#!usr/bin/env python
#coding:utf-8

'''

requests_test
leon
2017年10月15日

'''

import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import time
from lxml import html
from HTMLParser import HTMLParser
class Handle(object):
	
	def get_data(self):
		for i in range(10):
			url='https://movie.douban.com/top250?start=%d&filter='%(i*25)
			print url
			data=requests.get(url).content
			text=html.fromstring(data)
			title=text.xpath("//h1/text()")
			for item in text.xpath('//div[@class="item"]'):
				rank=item.xpath('div[@class="pic"]/em[1]/text()')[0]
				movie=item.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()')
				names=''
				for name in movie:
					#name=HTMLParser().unescape(name)
					name=name.replace('\xc2\xa0','')
					names=names+'/'+name
				link=item.xpath('div[@class="info"]/div[@class="hd"]/a/@href')[0]
				detail=item.xpath('div[@class="info"]/div[@class="bd"]/p[1]/text()')
				director=detail[0].replace(" ",'').replace("\n",'').replace("\xc2\xa0"," ")
				film_type=detail[1].replace(" ","").replace('\n',' ').replace("\xc2\xa0"," ")
				score=item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
				cnt=item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()')[0]
				with open('film_top250.txt','a') as file:
					file.write('''\n rank:%s name: %s \n director: %s \n film_tpye:%s \n score:%s cnt%s \n'''%(rank,names,director,film_type,score,cnt))
					file.write("==========================")

if __name__ =='__main__':
	Handle().get_data()

