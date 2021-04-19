from flask import Flask, render_template, url_for, request, redirect, flash, session
from website import app, db
from website.forms import IndexForm
from website.functions import Search

value = []
@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    form = IndexForm()
    if request.method == 'POST':
        if (form.validate_on_submit()):
            value.extend(request.form.get("price"))
            value.extend(request.form.get("factory_system"))
            value.extend(request.form.get("phone_screen"))
            value.extend(request.form.get("phone_OS"))
            value.extend(request.form.get("phone_resolution"))
            value.extend(request.form.get("phone_frequency"))
            value.extend(request.form.get("phone_kernel_num"))
            value.extend(request.form.get("phone_RAM_capacity"))
            value.extend(request.form.get("phone_ROM_capacity"))
            value.extend(request.form.get("phone_battery_capacity"))
            value.extend(request.form.get("phone_rear_camera"))
            value.extend(request.form.get("phone_front_camera"))
            return redirect(url_for('result'))
        else:
            flash("wrong")

    return render_template('index.html',form=form)


@app.route('/result')
def result():
    data = Search(value)
    print(data)
    return render_template('result.html',data=data)


