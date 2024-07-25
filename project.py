'''CST205 -- Room Decor Quiz Group Project'''

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from function import maxIndex
#index to count the clicks on the images.
index_count = [0,0,0,0]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

#Displays the first page of the application. -Prayash Raj Singh.
@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
#Gets the title and page from the html and keeps track of the number of clicks made on 
#the specific image type. Depending on the previous page number it will display the upcoming page. And while
#at the end of the page, it will see the highest number of index count and displays the information for that
#image type. - Prayash Raj Singh.
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
        for i in range(4):
            index_count[i]=0
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
