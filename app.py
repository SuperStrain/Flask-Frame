from flask import Flask
#debug模式的开启

app = Flask(__name__)

#路由解析，通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

@app.route('/index')
def hello():
    return "您好"

if __name__ == '__main__':
    app.run()
