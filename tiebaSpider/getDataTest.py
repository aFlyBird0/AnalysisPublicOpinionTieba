
from weiboSpider import weibo
keyword= "1"
page = 1
sina_weibo = weibo.weibo()
result = sina_weibo.search(context=keyword, pages=page)
print(result)