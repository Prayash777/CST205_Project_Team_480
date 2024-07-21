from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route('/minimalism')
def minimalism():
    return render_template('minimalism.html')

@app.route('/cyber_punk')
def cyber_punk():
    return render_template('cyber_punk.html')

@app.route('/earthy')
def earthy():
    return render_template('earthy.html')

@app.route('/grunge')
def grunge():
    return render_template('grunge.html')