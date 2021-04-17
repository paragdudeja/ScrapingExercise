# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class CasestudyinfoPipeline:
	def __init__(self):
		self.conn = pymongo.MongoClient("mongodb+srv://admin-parag:test123@cluster0.gq3uj.mongodb.net/test")

		db = self.conn['scrap_data']
		self.collection = db['case_studies']
		self.collection.drop()
		db = self.conn['scrap_data']
		self.collection = db['case_studies']

	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item
