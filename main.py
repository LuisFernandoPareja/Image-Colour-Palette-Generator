from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from ColorGenerator import test_funct

app = Flask(__name__)
Bootstrap5(app)


@app.route('/')
def home():
    return render_template('index.html', num=test_funct())




if __name__ == '__main__':
    app.run(debug=True)
