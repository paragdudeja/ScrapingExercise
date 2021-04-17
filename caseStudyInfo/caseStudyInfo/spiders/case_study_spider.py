import scrapy
import re
from ..items import CasestudyinfoItem

class CaseStudySpider(scrapy.Spider):
	name = 'case_studies'
	start_urls = [
		'https://www.astutewales.com/en/case-studies'
	]
	count = 0
	def parse(self, response):
		item = CasestudyinfoItem()

		all_case_studies = response.css(".casestudy")

		for case_study in all_case_studies:
			title = case_study.css(".casestudy__title::text").extract()
			detail_link = case_study.css(".casestudy__link::attr(href)").get()

			item['title'] = title
			item['detail_link'] = detail_link

			request = scrapy.Request(response._url[:-13] + '/' + detail_link,callback=self.parse_page2)
			request.meta['item'] = item

			yield request

	def parse_page2(self, response):
			item = response.meta['item']
			
			challenge = "NA"
			solution = "NA"

			page_text = response.xpath("//div[@class='grid']//text()").extract()

			index1 = index2 = index3 = 0

			try:
				regex = re.compile("^Challenge")
				idxs = [i for i, item in enumerate(page_text) if re.search(regex, item)]
				
				index1 = idxs[0]

				regex = re.compile("^Solution")
				idxs = [i for i, item in enumerate(page_text) if re.search(regex, item)]
				index2 = idxs[0]

				regex = re.compile("^Impact")
				idxs = [i for i, item in enumerate(page_text) if re.search(regex, item)]
				index3 = idxs[0]
			except Exception as e:
				pass
			

			

			item['title'] = response.css(".casestudy--top h3::text").extract()[0].strip()
			item['detail_link'] = response._url

			challenge_extract = [x for x in page_text[index1+1:index2] if '\r' not in x ]
			challenge = " ".join(challenge_extract)
			solution_extract = [x for x in page_text[index2+1:index3] if '\r' not in x ]
			solution = " ".join(solution_extract) 

			if challenge == "":
				challenge = "NA"

			if solution == "":
				solution = "NA"

			business = response.css(".casestudy--business::text").extract()[0]
			expertise = response.css(".casestudy--single--content p::text").extract()[0]

			item['challenge'] = challenge
			item['solution'] = solution
			item['business'] = business
			item['expertise'] = expertise

			yield item


	
