# -*- coding=utf-8 -*-
import urllib
import urllib2
import re
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

page = raw_input(u"Pages to download: ")

fname = "qsbk.txt"
text = open(fname,'wb')
for i in range(int(page)):

    page = i
    url = "http://www.qiushibaike.com/hot/page/" + str(page)
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    headers = {"User-Agent":user_agent}

    try:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
    except urllib2.URLError,e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

    content = response.read().decode('utf-8')
    pattern = re.compile('div.*?author clearfix">.*?<a.*?title=.*?<h2.*?>(.*?)</h2>.*?</a>.*?<div.*?' +
                     'content">.*?span>(.*?)</span>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item[0]
        print item[1],os.linesep
        content = item[0]+os.linesep+item[1]
        text.write(item[0]+"\r\n")
        text.write(item[1]+"\r\n"+"\r\n")
        text.write( "\r\n")
text.close()