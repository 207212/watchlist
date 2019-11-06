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


'''from flask import Flask
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

