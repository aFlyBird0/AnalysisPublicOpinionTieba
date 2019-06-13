from weiboSpider.Web import Web
import time
import re

import requests
from lxml import etree


class Weibo(Web):
    def __int__(self):

        super.__int__(self)
        self.href = None
        self.page = None
        self.q = None
        self.author = None
        self.text = None
        self.card = None

    def url_create(self, test, page):
        super.url = "https://s.weibo.com/weibo?q=%s&Refer=g&page=%d" % (test, page)

    def g(self):
        self.get_response()
        self.get_html_text()
        self.get_etree()
        self.get_html_content()

    def search(self, context, pages):
        self.card = []
        for page in range(1, pages + 1):
            self.set_url("https://s.weibo.com/weibo?q=%s&Refer=g&page=%d" % (context, page))
            self.g()
            names = self.tree.xpath('//div[@class="card-feed"]/div[@class="content"]//a[@class="name"]/text()')
            i = 0
            for name in names:
                txt = self.tree.xpath('//div[@class="card-feed"]/div[@class="content"]//p[@class="txt"]')[i]
                i = i + 1
                info = txt.xpath('string(.)')
                m = []
                m.extend(info)
                s = ''.join(m)
                y = [name, s]
                self.card.append(y)


if __name__ == '__main__':

    w = Weibo()
    w.author = []
    w.text = []
    # sum = 1
    w.search('杭州电子科技大学', 3)
    #    print(w.card)
    for ca in w.card:
        print(ca)

'''    w.q=input("请输入宁要搜索的内容：")
    for w.page in range(1,2,1):
        w.set_url("https://s.weibo.com/weibo?q=%s&Refer=g&page=%d"%(w.q,w.page))
        print(w.get_url())
        w.g()
        names=w.tree.xpath('//div[@class="card-feed"]/div[@class="content"]//a[@class="name"]/text()')
#        l=w.tree.xpath('//p[@class="from"]/a[@target="_blank"]/@href')
        i=0
        for name in names:
            txt = w.tree.xpath('//div[@class="card-feed"]/div[@class="content"]//p[@class="txt"]')[i]
            i=i+1
            info = txt.xpath('string(.)')
            m=[]
            m.extend(info)
            s = ''.join(m)
            y=[name,s]
            w.card.append(y)
        time.sleep(3)
        break
    for ca in w.card:
        print(ca)
#    print(type(s))'''
'''    for href in w.froms:
        child=weibo()
        child.set_url("https:"+href+"&type=comment")
        print(child.get_url())
        child.g()
        print(child.html_text)
        break
        pattern=re.compile("\\$CONFIG\\['onick'\\]='(.*?)';")
#        result=pattern.search(child.html_text())
#        print (result.group())
        time.sleep(2)
'''
