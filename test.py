#pip3 install Flask

from flask import Flask, render_template, request, url_for
import os,sys

app = Flask(__name__,template_folder='.')

# ---- en utilisant tous les pages pour tester l'affichage du pageB --
path = "pages_web";
dirs = os.listdir(path)
dic={}
i=0
for file in dirs:
#  	print(file)
	dic[file]=i
	i=i+1
# --------------------------------------------------------------------
@app.route("/")
@app.route("/pageA")
def pageA():
		return render_template('pageA.html')

@app.route("/pageB",methods=['POST'])
def pageB():
	result = request.form
	''' la partie qui a besoin du index_inversé
	index = ii.index_inverse(score = "log")
	index.compute()
	dic= index.ten_first(result)
	'''
	length = len(dic)
	return render_template('pageB.html',length=length,result=result,posts=dic)

if __name__ == '__main__':
   app.run(debug = True)


