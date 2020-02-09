from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def adam_main():
    return render_template("index_2.html")


@app.route('/1')
def miniport_main():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
