from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def miniport_main():
    return render_template("index.html")

@app.route("/main")
def hello_world():
    return 'Hello World!'


@app.route('/abc')
def test():
    return "ABC"

@app.route("/def")
def test2():
    return render_template("dataform.html")




if __name__ == '__main__':
    app.run()
