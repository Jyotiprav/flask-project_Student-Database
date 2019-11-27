#Flask  is the prototype used to create instances of web application
from flask import Flask, flash, redirect, url_for
from flask import render_template
from config import Config
from forms import LoginForm, addinfo, searchinfo
import sqlite3 as sql
#__name__ is a special variable that gets as value the string "__main__" when you’re executing the script.
app = Flask(__name__)
app.config.from_object(Config)
#------------------------------------#
#        Index/Home Page
#------------------------------------#
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Admin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Flask is simpler than Django '
        },
        {
            'author': {'username': 'Susan'},
            'body': 'This application is so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

#------------------------------------#
#             Login Page
#------------------------------------#
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    L=False
    if form.validate_on_submit():
        with sql.connect("info_db.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("select * from information")
            rows = cur.fetchall()
            for r in rows:
                if form.username.data == r['username'] and form.password.data==r['password']:
                    L=True
                    break
            if L==True:
                flash('Login Successful')
            else:
                flash('Login Unsuccessful Try Again')
            con.commit()
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
#------------------------------------#
#     Add Information Page
#------------------------------------#
@app.route('/Add', methods=['GET', 'POST'])
def Add():
    form = addinfo()
    if form.validate_on_submit():
        flash('Information Added')
        with sql.connect("info_db.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO information (username, password, email, phoneno) VALUES(?, ?, ?, ?)",(form.username.data,form.password.data,form.email.data,form.phoneno.data) )
            con.commit()
        return redirect(url_for('index'))
    return render_template('add_info.html', title='Add Your Information', form=form)

#------------------------------------#
#     Show Information Page
#------------------------------------#
@app.route('/show', methods=['GET','POST'])
def show():
    with sql.connect("info_db.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from information")
        rows = cur.fetchall()
    return render_template('show.html', title='Show', rows=rows)
#------------------------------------#
#     Search Information Page
#------------------------------------#
@app.route('/search', methods=['GET','POST'])
def search():
    form = searchinfo()
    L=False
    if form.validate_on_submit():
        with sql.connect("info_db.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("select * from information")
            rows = cur.fetchall()
            for r in rows:
                if form.username.data == r['username']:
                    #L=True
                    return render_template('search1.html', title='Search', r=r)
                    '''break
            if L==True:
                return render_template('search1.html', title='Search', row=r)
            else:
                flash('Login Unsuccessful')'''
            con.commit()
        return redirect(url_for('index'))
    return render_template('search.html', title='Search', form=form)

if __name__=='__main__':
    app.run()