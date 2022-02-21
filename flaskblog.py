from crypt import methods
from flask import Flask, render_template, url_for, flash, redirect
from forms import registration_form, login_form

app = Flask(__name__)

app.config['SECRET_KEY'] = '16d26700615533b17cf1eb2c74822d5805cafedf52640a33965e96d9ed88a093'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/pandas")
def pandas():
    return render_template('pandas.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = registration_form()
    if form.validate_on_submit():
        flash(f'Account Created For {form.username.data}!', 'success')
        return redirect(url_for('home'))  
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = login_form()
    return render_template('login.html', title='Login', form=form)

# This MUST live beneath all other content!!
if __name__ == '__main__':
    app.run(debug=True)



