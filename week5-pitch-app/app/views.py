from flask import render_template
from app import app, forms
from .forms import ReviewForm


# Views
@app.route('/', methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    form = ReviewForm()
    title = "Picth App"

    return render_template('index.html', title = title, review_form = forms)