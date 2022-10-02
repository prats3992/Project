#add these to html file under <head></head>
#<link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
#<script defer src="https://pyscript.net/latest/pyscript.js"></script>
from flask import Flask,render_template,url_for,request
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/result",methods=["POST","GET"])
def result():
    output=request.form.to_dict()
    name=output["name"]
    return render_template("index.html",name=name)
if __name__=='__main__':
    app.run(debug=True,port=5002)