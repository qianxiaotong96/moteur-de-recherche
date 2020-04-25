#!/usr/bin/python3.8
#incoding:utf-8
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("cherche"):
	username = form.getvalue("cherche")
else:
	raise Exception("Pseudo non transmis")


print("Content-type:text/html;charset=utf-8\n")

html = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Resultat</title>
	<style type="text/css">
	
		span{
			font-family: Georgia;
			font-weight: bold;
			font-size: 20px;
			text-shadow:#f3f3f3 1px 1px 0px, #b2b2b2 1px 2px 0;
			color: deepskyblue;	
		}

		i{
			color:orange;
		}

		#text{
			height:30px;
			border:1px solid grey;
			border-radius: 5px;
			width:50%; 
			text-align:center;
		}

		#submit{
			  background-color: #4CAF50;
  			  border: none;
  			  color: white;
  	          padding: 7px 7px;
              text-decoration: none;
              margin: 1px 1px;
              cursor: pointer;
              border-radius: 5px;
		}

		.recherche{
			width:100%; 
			position: absolute;
			top: 5%;
			left: 50%;
			-webkit-transform: translate(-50%, -50%);
			-moz-transform: translate(-50%, -50%);
		}

		#resultat{
			margin-left:20px;
		}

		p{
			font-size:small;
		}

		</style>
</head>
<body>
	<div class="all">
	<form method="post" action="" class="recherche"><span>Recherche <i>Gr6  </i></span><input id="text" type="text" name="cherche" placeholder="entrez ce que vous voulez chercher"><input id="submit" type="submit" value="Valider">
	</form>
	</div>
	</br>
	</br>
	</br>
	<hr>
"""
print(html)
print(f"vous cherchez : {username}")
nbre = 6
print(f" (environ {nbre} résultats ont été trouvés)")
html2="""
	<div id="resultat">
	<div>
	<a href="#">Resultat1 </a>
	<p> Contenu1 </p>
	</div>
	<div>
	<a href="#">Resultat2 </a>
	<p> Contenu2 </p>
	</div>
	<div>
	<a href="#">Resultat3 </a>
	<p> Contenu3 </p>
	</div>
	<div>
	<a href="#">Resultat4 </a>
	<p> Contenu4 </p>
	</div>
	<div>
	<a href="#">Resultat5 </a>
	<p> Contenu5 </p>
	</div>
	<div>
	<a href="#">Resultat6 </a>
	<p> Contenu6 </p>
	</div>
	</div>
</body>
</html>
"""

print(html2)





