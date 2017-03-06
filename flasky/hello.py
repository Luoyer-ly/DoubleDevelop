#encoding='utf-8'
from flask import Flask,url_for
from flask import make_response
from flask import redirect
from flask import abort
#from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment,datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
#manager = Manager(app)

@app.route("/")
def index():
	#return redirect('http://www.bing.com')
    #return "<h1>Hello World!</h1><br><a href='/user/luo'>jump</a>"
    #return '<h1>Bad Request</h1>',400
    #response = make_response('<h1>This document carries a cookie!</h1>')
    #response.set_cookie('answer','42')
    #return response
    #name = ['23','56','78']
    #lnk = url_for('user',name='john')
    #print url_for('static',filename='favicon.ico')
    return render_template('index.html',current_time=datetime.utcnow())
    #return render_template('index.html',comments=name,jmp_link=lnk)
@app.route("/user/<name>")
def user(name):
	#return "<h2>hello, %s</h1>" % name
	ext_name = ['23','46','78']
	ext_name.append(name)
	return render_template('user.html',name=ext_name)
#@app.route("/user/<id>")
#def get_user(id):
#	user = load_user(id)
#	if not user:
#		abort(404)
#	return "<h3>hello,%s</h3>" %user.name
@app.route("/test_base")
def test_bs():
	return render_template("ext_base.html")


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

if __name__ == "__main__":
	app.run(debug=True)
    #app.run(debug=True)
    #manager.run()
