from flask import Flask,render_template,url_for,request
from whatspp_project import recaptcha
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("whatspp.html")
@app.route("/result",methods=["POST","GET"])
def result():
    output=request.form.to_dict()
#    name=output["name"]
#    return render_template("whatspp.html",name=name)
    ...
if __name__=='__main__':
    app.run(debug=True,port=5002)