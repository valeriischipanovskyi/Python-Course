import redis as redis
from flask import Flask, render_template, request, redirect, session, g

app = Flask(__name__)

@app.before_request
def b_r():
    g.r = redis.StrictRedis()

@app.route('/')
def index():
    names = g.r.keys('phone:*')
    contacts = [(name[6:].decode('utf8'), g.r.get(name).decode('utf8')) for name in names]
    print(contacts)
    return render_template('Index.html',
                           message=session.pop('message'),
                           contacts=contacts
                           )

@app.route('/<add>', methods=['GET', 'POST'])
def add():
    name = phone_number = ''
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']
        if name and phone_number:
            r = redis.StrictRedis()
            r.set("phone:" + name, phone_number)
            session['mesage'] = "Contact successfully added"
            return redirect('/')
    return render_template('Add.html', name=name, phone_number=phone_number)

app.run(debug=True)
