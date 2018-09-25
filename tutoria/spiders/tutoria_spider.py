# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class TutoriaSpider(scrapy.Spider):
	name = "tutoria"
	allowed_domains = ["dmoz.org"]
	start_urls = [
			"http://www.dmoz.org/Computers/Programming/Langguages/Python/Books/",
			"http://www.dmoz.org/Computers/Programming/Langguages/Python/Resources/"
			]
			
	def parse(self,response):
		filename = response.url.split("/")[-2]
		with open(filename,'wb') as f:
			f.write(response.body)