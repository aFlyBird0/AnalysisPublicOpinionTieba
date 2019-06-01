# 百度贴吧™爬虫 和 情感分析



## 2019/06/01

update：

1. 新增了前端文件，支持直接在前端页面进行输入和点选等操作，完成爬虫的爬取和情感评级
   + 该文件位于`template` 文件夹下，为`simple_index.html`.
   + 使用方法：
     + 运行f`lask_tiebaSearch_demo.py`，浏览器访问：http://127.0.0.1:5000/ ，即可使用





## 2019/06/01 之前的更新

* 简单爬虫（返回列表，其中每一篇文章是字典）

* 情绪分析接口（传入content,自动请求返回json或dict）

* 仅爬取第一层，得到字典，并且每篇文章加入情感结果

  ```json
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
  ```

* 针对只爬第一楼的情况又重新分析网页做了针对性的优化，极大提高了爬取速度，同时删去相对无用的"作者"信息，删去之前写的已经用不到的函数，减小代码体积