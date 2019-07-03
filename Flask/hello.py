from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/utkarsh')
def utkarsh():
    return '<h1> Hey I am Utkarsh Anand</h1>'

@app.route('/student/<name>')
def student(name):
    return 'Hey there %s' %name
if __name__ == '__main__':
    app.run()
