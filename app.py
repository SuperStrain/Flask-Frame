#总共要学两步，
# 第一步定义好路径，
# 第二步利用render_template返回html文件


from flask import Flask,request,render_template#render_template为渲染模板
import datetime
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
    time=datetime.date.today()  #普通变量
    name=["张三","李四","王二麻子"] #列表类型
    task={"任务":"打扫卫生","时间":"3个小时"}#字典类型
    return render_template("text.html",var=time,list=name,task=task)

#表单提交
@app.route('/text/register')
def register():
    return render_template('text/register.html')

#接受表单提交的路由需要指定method为post
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template('text/result.html',result=result)

if __name__ == '__main__':
    app.run()
