#!/usr/bin/python
#coding:utf-8
import cgi

print("Content-type:text/html;charset=utf-8\n")

html = """<!DOCTYPE html>
<html>
<head>
	<title>Cherche</title>
	<style type="text/css">
	
		h1{
			font-family: Georgia;
			text-shadow:#f3f3f3 1px 1px 0px, #b2b2b2 1px 2px 0;
			color: deepskyblue;
			position: absolute;
			top: 40%;
			left: 50%;
			-webkit-transform: translate(-50%, -50%);
			-moz-transform: translate(-50%, -50%);
			-ms-transform: translate(-50%, -50%);
			-o-transform: translate(-50%, -50%);
			transform: translate(-50%, -50%);		
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
			width:100%; text-align:center;
				position: absolute;
				top: 55%;
				left: 50%;
				-webkit-transform: translate(-50%, -50%);
				-moz-transform: translate(-50%, -50%);
		}


	</style>
</head>
<body>
	<script type="text/javascript">
		function jump(){
			if(document.getElementById('text').value)
				document.form.action = "pageB.py";
			else
				document.form.action = "pageA.py";
		}
	</script>
	<div class="all">
		<h1> Recherche <i>Gr6</i></h1>
	<form name="form" method="post" action="" class="recherche">
		<input id="text" type="text" name="cherche" placeholder="entrez ce que vous voulez chercher"><input id="submit" type="submit" value="valider" onclick="jump()">
	</form>
	</div>
</body>
</html>
"""

print(html)
