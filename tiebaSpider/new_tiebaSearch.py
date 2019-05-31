from flask import Flask, request, render_template, redirect, url_for
import time
from tiebaSpider import tieba3, spiderOnlyFirstFloorAdvance
from SentimentAnalysis import Analysis

app = Flask(__name__)

users = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('new_html.html', says=users)

    else:
        users.clear()

        context = request.form.get('context')
        page = request.form.get('page')
        print(context)
        print(page)
        result = spiderOnlyFirstFloorAdvance.get_list_first_floor_advance(page_want=int(page), keyword=context)
        for res in result:
            print(res['firstFloorContent'])
            emotion = Analysis.analysis_Dict(res['title'])['items'][0]['positive_prob']
            if emotion >= 0.75:
                emotion_type = '非常积极'
            elif emotion >= 0.5 and emotion < 0.75:
                emotion_type = '积极'
            elif emotion >= 0.3 and emotion < 0.5:
                emotion_type = '有点消极'
            elif emotion < 0.3:
                emotion_type = '非常消极'
            users.append(
                {"text": res['firstFloorContent'], "title": res['title'], "href": res['href'], "emotion": emotion_type})

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, )
