#总共要学两步，第一步定义好路径，第二步利用render_template返回html文件


from flask import Flask,render_template #渲染模板
#debug模式的开启

app = Flask(__name__)


#通过访问路径，获得用户的字符串参数
@app.route('/user/<name>')
def welcome1(name):
    return "欢迎您%s"%name

#通过访问路径，获得用户的整型参数（此为还有float类型）
@app.route('/user/<int:id>')
def welcome2(id):
    return "您好，%d 号会员"%id


@app.route('/')
def tetx():
    return render_template("text.html")

if __name__ == '__main__':
    app.run()
