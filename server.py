from flask import Flask, render_template, request, url_for
#import celui du index_inversé
from Yacine import index_inverse as ii
#import os,sys

app = Flask(__name__,template_folder='.')

@app.route("/")
@app.route("/pageA")
def pageA():
		return render_template('pageA.html')

@app.route("/pageB",methods=['POST'])
def pageB():
	#appliquer la partie index_inversé
	result = request.form
	index = ii.index_inverse(score = "log")
	index.compute()
	dic= index.ten_first(result)
	length = len(dic)
	return render_template('pageB.html',length=length,result=result,posts=dic)

@app.route("/home")
def home():
	return render_template('home.html',posts=dic)

if __name__ == '__main__':
   app.run(debug = True)


