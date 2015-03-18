__author__ = 'Jayden'
#-*- coding: utf-8 -*-
import urllib2
import sys
from bs4 import BeautifulSoup
import datetime

def get_url(url):
	req_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:2.0) Gecko/20100101 Firefox/4.0', 'Referer':'http://python.org'}
	request = urllib2.Request(url, headers=req_headers)
	opener = urllib2.build_opener()
	response = opener.open(request)
	contents = response.read()
	return contents.encode('utf-8')

def get_tag(num):
    url = 'http://top-hashtags.com/instagram/' + num + '/'
    data = get_url(url)
    soup = BeautifulSoup(data, from_encoding="utf-8")
    contents = soup.findAll('a',{'class':'green button'})
    n = 0
    while n < len(contents):
        temp = contents[n].text
        tag = temp.replace("#",'')
        print tag.encode('utf-8')
        n = n + 1

i = 1
while i < 19902:
    get_tag(str(i))
    i = i + 100
