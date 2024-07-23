'''CST205 -- Room Decor Quiz Group Project'''

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from function import maxIndex
from image_info import image_list

index_count = [0,0,0,0]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)
@app.route('/', methods=('GET', 'POST'))
def index():    
    return render_template('index.html')

@app.route('/<title><page>')
def index1(title, page):
    print (title, page)
    if title == "cyber":
        index_count[0]+=1
    if(title == "earthy"):
        index_count[1]+=1
    if(title == "grunge"):
        index_count[2]+=1
    if(title == "minimalist"):
        index_count[3]+=1

    if(page == '1'):
        return render_template('index2.html')
    if(page == '2'):
        return render_template('index3.html')
    if(page == '3'):
        index = maxIndex(index_count)
        print(index_count)
        print(index)
        if(index == 0):
            return render_template('cyber_punk.html')
        elif(index == 1):
            return render_template('earthy.html')
        elif(index == 2):
            return render_template('grunge.html')
        elif(index == 3):
            return render_template('minimalism.html')
        else:
            return render_template('index.html')
    else:
        render_template('index.html')



print(index_count)
    

@app.route('/minimalism')
def minimalism():
    return render_template('minimalism.html')

@app.route('/cyber_punk')
def cyber_punk():
    return render_template('cyber_punk.html')

