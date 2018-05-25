from flask import Flask, render_template, request, redirect, url_for, session
from models.collection import Service, User, Order
import mlab

mlab.connect()
app = Flask(__name__)
#sesion
app.secret_key = 'This is secret key'

@app.route('/')
def service():
    service_list = Service.objects() # kéo dlieu tu collection ve
    return render_template('service.html',service_list = service_list)

@app.route('/detail/<user_id>', defaults={'customerid': "#", 'fullname':'#'}) # app.route là tên file chạy
@app.route('/detail/<user_id>/<customerid>/<fullname>')
def detail(user_id, customerid, fullname ):
    service_dict = Service.objects.with_id(user_id)
    return render_template('detail.html', item = service_dict,serviceid = user_id, customerid = customerid ,fullname = fullname)

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

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user_list = User.objects()
        form = request.form
        username = form['username']
        password = form['password']
        for item in user_list:
            if item['username'] == username and item['password'] == password:
                userid = item['id']
                session[str(userid)] = True # kiểm tra nếu password vs username đúng thì tạo một key trong dictionary tượng trưng cho giấy thông hành
                username = item['fullname']

                service_list = Service.objects() #lấy dữ liệu của service truyền vào để render

                # truyền dữ liệu vào html service qua render không truyền hàm đc vì ảnh hương đến route
                return render_template('service.html',service_list = service_list, fullname = username, userid = str(userid), session = session)
            else:
                # return"username or password incorrect"
                return redirect(url_for('login', method = 'GET'))

@app.route('/logout/<userid>')
def logout(userid):
    del session[str(userid)]
    # return "logout successful"
    return redirect(url_for('service'))

@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']
        data = User(fullname = fullname, email = email, username = username, password = password)
        data.save()
        return redirect(url_for('login', method = 'GET'))

@app.route('/request_service/<serviceid>/<userid>')
def request_service(serviceid,userid):
    data = Order(serviceid = serviceid, userid = userid, is_accepted = False)
    data.save()
    return "order successful"

if __name__ == '__main__':
  app.run( debug=True)
