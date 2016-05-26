from urllib import request

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/<add>', methods=['GET', 'POST'])
def add():
    print(request.form)
    return render_template('Add.html')


app.run(debug=True)
