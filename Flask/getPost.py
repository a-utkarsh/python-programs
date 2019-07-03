from flask import Flask , request

app = Flask(__name__)

@app.route("/")

def index():
    return "method used: is %s" % request.method

@app.route("/get", methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        return "You are using Post"
    else:
        return "You are probably using get"


if __name__ == "__main__":
    app.run()
