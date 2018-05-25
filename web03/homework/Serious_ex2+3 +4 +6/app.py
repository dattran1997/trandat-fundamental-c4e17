from flask import Flask, render_template, request, redirect, url_for
from models.collection import Service
import mlab

mlab.connect()
app = Flask(__name__)


@app.route('/service')
def service():
    service_list = Service.objects() # kéo dlieu tu collection ve
    return render_template('service.html',service_list = service_list)

@app.route('/detail/<user_id>')
def detail(user_id):
    service_dict = Service.objects.with_id(user_id)
    return render_template('detail.html', item = service_dict)

@app.route('/add', methods = ['POST','GET']) #method sẽ nhận giá trị từ html
def add():
    if request.method == 'GET': # request là phương thức của mongoengine
        return render_template('add.html')
    elif request.method == 'POST':
        form = request.form  #kiểu form từ bên html

        name = form['name']
        yob = form['yob']
        phone = form['phone']
        if form['gender'] == 'male':
            gender = 1
        else:
            gender = 0

        new_service = Service(name = name, yob = yob, phone = phone, gender = gender)
        new_service.save()

        return redirect(url_for('service'))

@app.route('/update/<user_id>', methods = ['POST','GET'])
def update(user_id):
    service_dict = Service.objects.with_id(user_id) # tim dictionary của người cần Update
    if request.method == 'GET':
        return render_template('update.html',item = service_dict)
    elif request.method == 'POST':
        service_list = Service.objects(id = user_id)
        form = request.form

        name = form['name']
        yob = form['yob']
        phone = form['phone']
        if form['gender'] == 'male':
            gender = 1
        else:
            gender = 0

        service_list.update(set__name= name, #hàm update chỉ hoạt động vs List
                            set__yob= yob ,
                            set__phone= phone ,
                            set__gender = gender)

        return redirect(url_for('service'))
        # return redirect({{url_for('detail',user_id = user_id)}})
        # return 'update successful'

if __name__ == '__main__':
  app.run( debug=True)
