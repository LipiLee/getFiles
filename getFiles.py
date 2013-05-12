#! /usr/bin/env python

import urllib2, string
from HTMLParser import HTMLParser

filename = 'KIES_HOME_E160SKSJMC4_1034927_REV02_user_low_ship.tar.7z'
href = ''

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global href
		if tag == 'a':
			for attr in attrs:
				if attr[0] == 'href':
					href = attr[1]
	def handle_data(self, data):
		global href
		if(string.find(data, filename) != -1):
			if(href != ''):
				print href
				print data
				zipfile = urllib2.urlopen(href)
				output = open(data, 'wb')
				output.write(zipfile.read())
				output.close()
				href = ''
		
parser = MyHTMLParser()
parser.feed(urllib2.urlopen('http://azdesigntm.tistory.com/285').read())
