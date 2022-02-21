from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    return render_template("index.html",
        title = 'Home',
        user = user)

@app.route('/about/<string:name>/<age>')
def about(name,age):
    return '<h1>Hello, About page! name:'+str(name) + ' age: ' + str(age) + '</h1>'


if __name__ == "__main__":
    app.run(debug=True) 