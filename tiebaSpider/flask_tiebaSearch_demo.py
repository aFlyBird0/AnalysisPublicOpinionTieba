from flask import Flask, request, render_template, redirect, url_for, make_response
from tiebaSpider import spiderOnlyFirstFloorAdvance
from SentimentAnalysis import Analysis
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    users = []
    if request.method == 'GET':
        return render_template('simple_index.html', says=users)

    else:
        users.clear()  # 清除输入框中的内容，方便下一次查询时输入

        context = request.form.get('context')  # 获取需要查询的文本关键字
        page = request.form.get('page')  # 获取需要查询的帖子页面数
        print(context)
        print(page)
        result = spiderOnlyFirstFloorAdvance.get_list_first_floor_advance(page_want=int(page), keyword=context)
        for res in result:
            print(res['firstFloorContent'])
            emotion = Analysis.analysis_Dict(res['title'])['items'][0]['positive_prob']  # 调用百度的”情感分析API“，返回文本的情感极性值
            if emotion >= 0.800:  # 对返回的值进行一个登记划分，以 20% 为一档
                emotion_type = "非常积极"
            elif 0.600 <= emotion < 0.800:
                emotion_type = "较为积极"
            elif 0.400 <= emotion < 0.600:
                emotion_type = "中性情感"
            elif 0.200 <= emotion < 0.400:
                emotion_type = "较为消极"
            elif emotion < 0.200:
                emotion_type = "非常消极"
            users.append(
                {"text": res['firstFloorContent'], "title": res['title'], "href": res['href'], "emotion": emotion_type})

        return redirect(url_for('index'))


@app.route('/tieba', methods=['GET', 'POST'])  # 定义路由(Views)，可以理解为定义页面的URL
def show_tieba_index():
    return render_template('tieba_monitor_index.html', )


@app.route('/weibo', methods=['GET', 'POST'])  # 定义路由(Views)，可以理解为定义页面的URL
def show_weibo_index():
    return render_template('weibo_monitor_index.html', )


@app.route('/tiebaInfo', methods=['GET', 'POST'])
def get_tieba_info():
    """
    调用前面写好的爬虫方法 和 情感分析接口
    对情感分析返回的值，自己手动设置一个阶梯，按照 20% 来划分层次
    等待改进的点：每次爬取的时间比较长，需要等待一段时间才能返回结果
    :return:
    """
    page = int(request.args.get('page'))  # 别问这个啥用处，我也不清楚，胶水粘起来的，能跑……
    keyword = request.args.get('keyword')
    result = spiderOnlyFirstFloorAdvance.get_list_first_floor_advance(page_want=page, keyword=keyword)
    # result = spiderOnlyFirstFloorAdvance.get_json_first_floor_advance(page_order=page, keyword=keyword)
    for res in result:
        print(res['firstFloorContent'])
        emotion = Analysis.analysis_Dict(res['title'])['items'][0]['positive_prob']  # 调用百度的”情感分析API“，返回文本的情感极性值
        if emotion >= 0.800:  # 对返回的值进行一个登记划分，以 20% 为一档
            emotion_type = "非常积极"
        elif 0.600 <= emotion < 0.800:
            emotion_type = "较为积极"
        elif 0.400 <= emotion < 0.600:
            emotion_type = "中性情感"
        elif 0.200 <= emotion < 0.400:
            emotion_type = "较为消极"
        elif emotion < 0.200:
            emotion_type = "非常消极"
        res['emotion_type'] = emotion_type
        res['emotion'] = emotion

    result_json = json.dumps(result)
    print(result_json)
    rst = make_response(result_json)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    print(rst)
    return rst


# 加载更多部分请求的url路由
@app.route('/info_new', methods=['GET', 'POST'])
def get_info_new():
    """
    调用前面写好的爬虫方法 和 情感分析接口
    对情感分析返回的值，自己手动设置一个阶梯，按照 20% 来划分层次
    :return:
    """
    page = int(request.args.get('page'))  # 别问这个啥用处，我也不清楚，胶水粘起来的，能跑……
    keyword = request.args.get('keyword')
    result = spiderOnlyFirstFloorAdvance.quick_get_first_floor_advance(page_order=page, keyword=keyword)
    for res in result:
        print(res['firstFloorContent'])
        emotion = Analysis.analysis_Dict(res['title'])['items'][0]['positive_prob']  # 调用百度的”情感分析API“，返回文本的情感极性值
        if emotion >= 0.800:  # 对返回的值进行一个登记划分，以 20% 为一档
            emotion_type = "非常积极"
        elif 0.600 <= emotion < 0.800:
            emotion_type = "较为积极"
        elif 0.400 <= emotion < 0.600:
            emotion_type = "中性情感"
        elif 0.200 <= emotion < 0.400:
            emotion_type = "较为消极"
        elif emotion < 0.200:
            emotion_type = "非常消极"
        res['emotion_type'] = emotion_type
        res['emotion'] = emotion

    result_json = json.dumps(result)
    print(result_json)
    rst = make_response(result_json)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    print(rst)
    return rst


# @app.route('/weiboInfo', methods=['GET', 'POST'])
# def get_weibo_info():
#     """
#     调用前面写好的爬虫方法 和 情感分析接口
#     对情感分析返回的值，自己手动设置一个阶梯，按照 20% 来划分层次
#     等待改进的点：每次爬取的时间比较长，需要等待一段时间才能返回结果
#     :return:
#     """
#     page = int(request.args.get('page'))  # 别问这个啥用处，我也不清楚，胶水粘起来的，能跑……
#     keyword = request.args.get('keyword')
#     sina_weibo = weibo.weibo()
#     result = sina_weibo.search(context=keyword, page=page)
#     print(result)
#     # result = spiderOnlyFirstFloorAdvance.get_json_first_floor_advance(page_order=page, keyword=keyword)
#     """
#     for res in result:
#         print(res['firstFloorContent'])
#         emotion = Analysis.analysis_Dict(res['title'])['items'][0]['positive_prob']  # 调用百度的”情感分析API“，返回文本的情感极性值
#         if emotion >= 0.800:  # 对返回的值进行一个登记划分，以 20% 为一档
#             emotion_type = "非常积极"
#         elif 0.600 <= emotion < 0.800:
#             emotion_type = "较为积极"
#         elif 0.400 <= emotion < 0.600:
#             emotion_type = "中性情感"
#         elif 0.200 <= emotion < 0.400:
#             emotion_type = "较为消极"
#         elif emotion < 0.200:
#             emotion_type = "非常消极"
#         res['emotion_type'] = emotion_type
#         res['emotion'] = emotion
#
#     result_json = json.dumps(result)
#     print(result_json)
#     rst = make_response(result_json)
#     rst.headers['Access-Control-Allow-Origin'] = '*'
#     print(rst)
#     return rst
#     """
#     return result


if __name__ == '__main__':
    app.run(debug=True, )
