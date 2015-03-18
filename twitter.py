__author__ = 'Jayden'
#-*- coding: utf-8 -*-
import urllib2
import sys
from bs4 import BeautifulSoup
import datetime
import urllib

total = 1

def get_url(url):
    req_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:2.0) Gecko/20100101 Firefox/4.0', 'Referer':'http://python.org'}
    request = urllib2.Request(url, headers=req_headers)
    opener = urllib2.build_opener()
    try:
        response = opener.open(request)
    except urllib2.HTTPError, e:
        print '\033[1;31mHTTPError = ' + str(e.code) + '\033[1;m'
        return 'error'
    except urllib2.URLError, e:
        print '\033[1;31mURLError = ' + str(e.reason) + '\033[1;m'
        return 'error'
    except httplib.HTTPException, e:
        print '\033[1;31mHTTPException\033[1;m'
        return 'error'
    except Exception:
        import traceback
        checksLogger.error('generic exception: ' + traceback.format_exc())
        return 'error'

    contents = response.read()
    return contents.encode('utf-8')

def get_text(query, weburl):
    global total
    urlvalue = urllib.quote(query)
    url = weburl + urlvalue
    print '\033[1;36m' + url + '\033[1;m'
    data = get_url(url)
    if data is not 'error':
        print '\033[1;32mOK\033[1;m'
        soup = BeautifulSoup(data,from_encoding="utf-8")
        contents_t = soup.findAll('p',{'class':'js-tweet-text tweet-text'})
        n = 0
        while n < len(contents_t):
            tweet = contents_t[n].text
            lang = str(contents_t[n])
            lang = lang.split('lang="')[1]
            lang = lang.split('"')[0]
            #print '\033[1;34m' + lang + '\033[1;m'
            n = n + 1
            print '\033[1;35m' + str(total) + '\033[1;m'
            total = total + 1
            fs = query + '|' + lang + '|' + tweet 
            #print fs.encode('utf-8')
            fp.write(fs.encode('utf-8'))
            fp.write('\n============================================================\n')

    else:
        print '\033[1;31mERROR\033[1;m'

qn = 1
with open('tags') as f:
    lines = f.read().splitlines()
    fp = open('tweet','w')
    for tag in lines:
        print '\033[1;33m' + str(qn) + '\033[1;m'
        qn = qn + 1
        print '\033[1;34m' + tag + '\033[1;m'
        get_text(tag,'https://twitter.com/search?f=realtime&q=')
    fp.close()
