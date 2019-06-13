
from weiboSpider import Weibo
keyword= "1"
page = 1
sina_weibo = Weibo.weibo()
result = sina_weibo.search(context=keyword, pages=page)
print(result)