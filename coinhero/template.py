
message = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>

	<title>Jonathan Doe | Web Designer, Director | name@yourdomain.com</title>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />

	<meta name="keywords" content="" />
	<meta name="description" content="" />

	<link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/2.7.0/build/reset-fonts-grids/reset-fonts-grids.css" media="all" /> 
	<link rel="stylesheet" type="text/css" href="resume.css" media="all" />

</head>
<body>

<div id="doc2" class="yui-t7">
	<div id="inner">
	
		<div id="hd">
			<div class="yui-gc">
				<div class="yui-u first">
					<h1>
"""
message += resume.getName()


message += "</h1><h2>"

message += resume.getTitle()

message += """</h2>
				</div>

			</div><!--// .yui-gc -->
		</div><!--// hd -->
		

		<div id="bd">
			<div id="yui-main">
				<div class="yui-b">

					<div class="yui-gf">
						<div class="yui-u first">
							<h2>Education</h2>
						</div>
						<div class="yui-u">"""

eduLst = resume.get("edu") 

for i in eduLst:
	message += "<p class=\"\">" + i + "</p>"

message += """"</div>
					</div><!--// .yui-gf -->

					<div class="yui-gf">
						<div class="yui-u first">
							<h2>Technical Skills</h2>
						</div>
						<div class="yui-u">"""


skillLst = resume.get("skills")

count = 0
for j in skillLst:
	if count%3 == 0:
		message += """<ul class="talent">"""

	message += 	"<li class=\"last\">" + i + "</li>"

	if count%3 == 0 and count != 0:
		message += """</ul>"""


message +=""" 							
						</div>
					</div><!--// .yui-gf-->



					<div class="yui-gf">
	
						<div class="yui-u first">
							<h2>Work Experience</h2>
						</div><!--// .yui-u -->

						<div class="yui-u"> """


jobLst = resume.get("jobs")						

for k in jobLst:
		message += "<div class=\"job\">" + k + "</div>"

message += """
						</div><!--// .yui-u -->
					</div><!--// .yui-gf -->


					<div class="yui-gf last">
						<div class="yui-u first">
							<h2>Projects</h2>
						</div>
						<div class="yui-u"> """


projLst = resume.get("projects")						

for l in projLst:
		message += "<div >" + l + "</div>"


message += """ 							
						</div>
					</div><!--// .yui-gf -->


				</div><!--// .yui-b -->
			</div><!--// yui-main -->
		</div><!--// bd -->

		<div id="ft">
			<p>Jonathan Doe &mdash; <a href="mailto:name@yourdomain.com">name@yourdomain.com</a> &mdash; (313) - 867-5309</p>
		</div><!--// footer -->

	</div><!-- // inner -->


</div><!--// doc -->


</body>
</html> """



