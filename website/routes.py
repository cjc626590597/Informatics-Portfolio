from flask import Flask, render_template, url_for, request, redirect, flash, session
from website import app, db
from website.forms import IndexForm


@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    form = IndexForm()
    if(form.validate_on_submit()):
        return render_template('result.html',form=form)
    return render_template('index.html',form=form)

@app.route('/result')
def result():
    return render_template('result.html')


