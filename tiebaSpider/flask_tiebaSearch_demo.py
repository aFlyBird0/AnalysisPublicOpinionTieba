from flask import Flask, request, render_template, redirect, url_for, make_response
from tiebaSpider import tieba3, spiderOnlyFirstFloorAdvance
from SentimentAnalysis import Analysis
from flask_bootstrap import Bootstrap
import time
import json
import urllib

app = Flask(__name__)

bootstrap = Bootstrap(app)

users = []


@app.route('/', methods=['GET', 'POST'])
def index():
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


@app.route('/show', methods=['GET', 'POST'])  # 定义路由(Views)，可以理解为定义页面的URL
def show():
    # page = int(request.args.get('page'))
    # keyword = request.args.get('keyword')
    # result = tieba3.gogogoStringBr(page, keyword)
    # return render_template('show.html', page=page, keyword=keyword, result=result)
    # return render_template('info.html', page=page, keyword=keyword, result=result)
    # result = spiderOnlyFirstFloorAdvance.get_list_first_floor_advance(page_want=1, keyword="杭州电子科技大学")
    # return render_template('tieba_monitor_index.html', result=result)

    return render_template('tieba_monitor_index.html',)


@app.route('/info?page=<string:page>&keyword=<string:keyword>', methods=['GET', 'POST'])
def get_info(page, keyword):
    # page = request.args.get('page')
    # keyword = request.args.get('keyword')
    # page = 1
    # keyword = "杭州电子科技大学 三位一体"
    result = spiderOnlyFirstFloorAdvance.get_list_first_floor_advance(page_want=page, keyword=keyword)

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


if __name__ == '__main__':
    app.run(debug=True, )
