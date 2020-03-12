from flask import Flask,render_template,url_for,request
from flask_material import Material
from datetime import datetime
from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template,url_for, flash, redirect
#from SEProject.forms import RegistrationForm, LoginForm
from flask_material import Material


app = Flask(__name__)
Material(app)

app.config['SECRET_KEY']='a857f8519efef4804da35c967de0e430'
#to protect the application from cross site cookies , fraud attacks
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)





@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
