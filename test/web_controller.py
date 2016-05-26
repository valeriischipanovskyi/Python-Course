from db_model import app, Account, Phones
from flask.ext.wtf import Form
from flask import render_template, request
from wtforms.ext.sqlalchemy.orm import model_form

phones = Phones()
Form = model_form(Account, Form)


@app.route('/create')
def create():
    return render_template('new.html', form=Form())


@app.route('/new', methods=['GET', 'POST'])
def new():
    phones.add_contact(request.args.get('name'), request.args.get('phone'))
    return render_template('index.html', phones=phones.get_contacts())


app.run(debug=True)
