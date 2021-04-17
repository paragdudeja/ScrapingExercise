import scrapy

from ..items import GrantsinfoItem

class GrantsSpider(scrapy.Spider):
	name = 'grants'
	start_urls = [
		'https://www.ukri.org/opportunity/'
	]

	def parse(self,response):
		items = GrantsinfoItem()

		all_posts = response.css(".status-publish")

		for post in all_posts:
			fund_title = post.css("h3 a::text").extract()[0].strip()
			opportunity_status =  post.css(".opportunity-status__flag::text").extract()[0].strip()
			summary = post.css(".entry-content").extract()[0].replace("\n","")
			award_range = 'NA'

			table_data = post.css(".opportunity-cells::text").extract()
			if 'Award range: ' in table_data:
				award_index = table_data.index('Award range: ') + 1
				award_range = table_data[award_index] 

			items['fund_title'] = fund_title
			items['summary'] = summary
			items['opportunity_status'] = opportunity_status
			items['award_range'] = award_range

			yield items

		next_page = response.css(".next::attr(href)").get()

		if next_page is not None:
			yield response.follow(next_page, callback = self.parse)

