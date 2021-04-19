from flask import render_template, url_for, request, redirect, flash, send_from_directory
from website import app
from website.export.export import exportXML, exportJSON_LD
from website.forms import IndexForm
from website.functions import Search

value = []


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
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

    return render_template('index.html', form=form)


@app.route('/result', methods=['GET', 'POST'])
def result():
    form = IndexForm()
    data = Search(value)
    dataList = []
    for item in data:
        tmp = [item.Phone_id,
               item.Phone_name,
               item.Phone_price,
               item.Phone_factory_system_kernel,
               item.Phone_screen_size,
               item.Phone_OS,
               item.Phone_resolution,
               item.Phone_frequency,
               item.Phone_kernel_num,
               item.Phone_RAM_capacity,
               item.Phone_ROM_capacity,
               item.Phone_battery_capacity,
               item.Phone_rear_camera,
               item.Phone_front_camera,
               item.Phone_pic_URL,
               item.Phone_brand,
               item.Phone_target_group]
        dataList.append(tmp)
    exportXML(dataList)
    exportJSON_LD(dataList)
    if request.method == 'POST':
        print(1)
        if 'XML' in request.form:
            print('XML')
            return redirect(url_for('downloadXML'))
        elif 'JSONLD' in request.form:
            print('JSONLD')
            return redirect(url_for('downloadJSONLD'))
    print(2)
    return render_template('result.html', data=data, form=form)


@app.route('/downloadXML', methods=['GET', 'POST'])
def downloadXML():
    print('WEBXML')
    return send_from_directory(app.root_path + '/export/', 'phones.xml', as_attachment=True)
    pass


@app.route('/downloadJSONLD', methods=['GET', 'POST'])
def downloadJSONLD():
    print('WEBJSON')
    return send_from_directory(app.root_path + '/export/', 'phones.jsonld', as_attachment=True)
    pass
