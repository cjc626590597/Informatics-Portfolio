from flask import Flask, render_template, url_for, request, redirect, flash, session
from website import app, db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')


