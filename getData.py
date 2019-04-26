'''
@返回数据格式:
[{
		'authorName': '作者名',
		'firstFloorContent': '第一楼内容',
		'title': '标题',
		'href': 'http链接',
		'positive_prob': 积极性,
		'confidence': 可信度
	},

	{
		'authorName': '作者名',
		'firstFloorContent': '第一楼内容',
		'title': '标题',
		'href': 'http链接',
		'positive_prob': 积极性,
		'confidence': 可信度
	}
]

'''


from tiebaSpider import spiderOnlyFirstFloor as soff
from SentimentAnalysis import Analysis

def getContentAndSentimentDict(page=1, keyword="杭州电子科技大学"):
	articleList = soff.gogogo_list_first_floor(page, keyword)
	# 获取所有文章的信息的列表，每个数据元素格式如下

	'''
	{'authorName': '作者', 
	'firstFloorContent': '第一楼内容', 
	'title': '标题', 
	'href': 'http链接'}
	'''
	for article in articleList:
		sentimentDict = Analysis.analysisDict(article['firstFloorContent'])
		# 对每篇文章第一楼内容进行情感分析
		article['positive_prob'] = sentimentDict['items'][0]['positive_prob']
		# 积极性存回字典
		article['confidence'] = sentimentDict['items'][0]['confidence']
		# 积极性存回字典
		# print(article)
	return articleList

if __name__ == '__main__':
	page = 1
	keyword = "杭州电子科技大学 三位一体"
	dataList = getContentAndSentimentDict(page = page, keyword = keyword)
	# print(dataList)
	for data in dataList:
		print(data)
