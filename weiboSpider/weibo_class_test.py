from weiboSpider.Weibo import Weibo


def test_Weibo_spider(page, keyword):
    # keyword = "杭州电子科技大学"
    # page = 2

    weibo = Weibo()
    weibo.author = []
    weibo.tesx = []
    weibo.search(context=keyword, pages=page)
    '''
    for ca in weibo.card:
        print(ca)
    '''
    print(weibo.card)
    #info1 = weibo.card[0]

    # 只取第一个分析他返回的到底是什么
    # for i, info_detail in enumerate(info1):
    #     print(i, info_detail)


# 事实证明他每个文章返回的是列表
# 每个列表只有两个元素
# 第一个貌似是来源
# 第二个是所有剩下的

if __name__ == '__main__':
    test_Weibo_spider(page=1, keyword='杭州电子科技大学')
