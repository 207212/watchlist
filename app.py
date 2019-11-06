'''
from flask import Flask  # 从flask包导入Flask类
app = Flask(__name__)  # 实例化Flask类


@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'
    return u'欢迎来到我的 Watchlist!'
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return 'User:%s' % name


from flask import Flask
from flask import url_for
app = Flask(__name__)  # 实例化Flask类


@app.route('/')
def hello():
    return 'Hello'


@app.route('/user/<name>')
def user_page(name):
    return 'User:%s' % name


@app.route('/test')
def test_url_for():
    # 下面是一些调用示例：
    print(url_for('hello'))  # 输出：/
    print(url_for('user_page', name='j'))  # 输出：/user/j
    print(url_for('user_page', name='haha'))  # 输出：/user/haha
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多于的关键字参数，它们会被作为查询字符串附加到URL后面
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'
'''

from flask import Flask, render_template
app = Flask(__name__)

name = "Jay Chou"
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
