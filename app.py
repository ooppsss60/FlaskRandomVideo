import os, random
from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/webm')
def showVideo():
	webmList = os.listdir(path="static/webm")
	webmNumber = random.randint(0, len(webmList)-1)
	
	jsText = '''
	addEventListener("keydown", function(event) {
		if (event.keyCode == 13){
			window.location.reload();
		};
	});
	'''

	cssText = '''
	body {
		background-color: #000000;
	} 
	#video {
		object-fit: contain;
		position: fixed;
		width: 100%;
		height: 100%;
	}
	'''

	htmlText = '''
	<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<title>Random video</title>
	<style>
	%s
	</style>
	</head>
	<script>
	%s
	</script>
	<video controls="controls" id="video" preload="auto" autoplay="true">
		<source src="static/webm/%s">
	</video>
	''' % (cssText, jsText, webmList[webmNumber])
	
	return htmlText

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8081)
