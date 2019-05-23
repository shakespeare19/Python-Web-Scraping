import scrapy
import re #regular expressions
from pdf_url.items import PdfUrlItem #our custom item type
from scrapy.spiders import CrawlSpider, Rule #crawlspider stuff
from scrapy.linkextractors import LinkExtractor #crawlspider stuff

class PdfUrlSpider(CrawlSpider):
	
	# This name is required. It is how we refer to this PdfUrlSpider class on the command line.
	name = 'pdf_url'

	# Every link we look at MUST be a part of the adobe.com domain (i.e. contain "adobe.com" in it's url)
	allowed_domains = ['adobe.com', 'apache.org', 'apple.com']

	# This is the url we will start from (Check all the links on this webpage first, then go deeper)
	start_urls = ['https://www.adobe.com', 'https://www.apache.org', 'https://www.apple.com']

	# This Rule says:
	# 1. allow all links to be extracted
	# 2. call parse_httpresponse on each extracted link
	# 3. follow all links ("click" on them) so we can check all the links on THAT webpage too
	rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

	# Will be called on all links we extract (i.e. all links). Automatically gets the HTTP response for us
	def parse_httpresponse(self, response):
		
		# Only continue if we got a 200 success response
		if response.status != 200:
			return None

		# Current url we are crawling
		print(response.url)

		# Create a custom item to hold the specified data we scrape 
		item = PdfUrlItem()

		# Check if this url holds pdf content
		if b'Content-Type' in response.headers.keys():
			links_to_pdf = 'application/pdf' in str(response.headers['Content-Type'])
		else:
			return None

		# Check if content disposition exists in HTTP response header
		content_disposition_exists = b'Content-Disposition' in response.headers.keys()

		# If this webpage holds pdf content, scrape it
		if links_to_pdf:
			
			# Scrape filename from Content-Disposition, if available
			if content_disposition_exists:
				item['filename'] = re.search('filename="(.+)"', str(response.headers['Content-Disposition'])).group(1)
				item['url'] = response.url
			
			# Scrape filename from url, otherwise
			else:
				item['filename'] = response.url.split('/')[-1]
				item['url'] = response.url

		# If this webpage doesn't hold pdf content, just ignore it and let scrapy move on to the next link
		else:
			return None

		# Return our scraped data (have scrapy write it to the csv file)
		return item



