import sqlite3
from flask import Flask, render_template, request, redirect, session, g


app = Flask(__name__)

@app.before_request
def b_r():
    g.sl = sqlite3.connect('dbphone.db')

@app.route('/')
def index():
    names = g.sl.execute('SELECT * from dbphone')
    contacts = [name for name in names]
    print(contacts)
    return render_template('Index.html',
    #                        message=session.pop('message'),
                           contacts=contacts
                           )
@app.route('/add', methods=['GET', 'POST'])
def add():
    name = phone_number = ''
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']
        if name and phone_number:
            sl = sqlite3.connect('dbphone.db')
            sl.execute("INSERT INTO dbphone (name, Phone_number) VALUES ({});".format(name, phone_number))
            session['mesage'] = "Contact successfully added"
            return redirect('/')
    return render_template('Add.html', name=name, phone_number=phone_number)


# @app.teardown_appcontext
# def close_db():
#     if hasattr(g, 'dbphone'):
#         g.sqlite_db.close()
app.secret_key = 'SFKHJhere7868khjh'
app.run(debug=True)
