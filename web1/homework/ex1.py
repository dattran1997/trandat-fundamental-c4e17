from flask import Flask, render_template
app = Flask(__name__)


@app.route('/about_me')
def index():
    a = {
        'name':'Trần Đat',
        'age':'21',
        'hobbie':'game',
        'school':'hust'
    }
    return render_template('index.html',a = a )

@app.route('/school')
def school():
    return render_template('school.html')
if __name__ == '__main__':
  app.run( debug=True)
