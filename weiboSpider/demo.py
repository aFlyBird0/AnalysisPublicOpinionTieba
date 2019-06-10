from flask import Flask, request, render_template, redirect, url_for
import time
from weibo import weibo

app = Flask(__name__)

users = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', says=users)

    else:
        users.clear()
        w = weibo()

        context = request.form.get('context')
        w.search(context, 2)
        for ca in w.card:
            users.append({"text": ca[1], "user": ca[0], })
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, )
