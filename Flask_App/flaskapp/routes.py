from flask import render_template, url_for, flash, redirect
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Stock

stocks = [
    {
        'symbol': 'AAPL',
        'last': '$168.88',
        'gainLoss': '0.98%'
    },
    {
        'symbol': 'MSFT',
        'last': '$295.00',
        'gainLoss': '-1.25%'
    },
    {
        'symbol': 'TSLA',
        'last': '$875.76',
        'gainLoss': '0.12%'
    }
]

articles = [
    {
        'date': '1/31/2022',
        'time': '2 min ago',
        'source': 'New York Times',
        'title': 'Breaking news: Bitcoin goes negative!'
    },
    {
        'date': '1/31/2022',
        'time': '34 min ago',
        'source': 'The Economist',
        'title': 'SpaceX may be sending rockets to space, but TSLA is reaching the moon'
    },
    {
        'date': '1/30/2022',
        'time': '1 day ago',
        'source': 'Wall Street Journal',
        'title': 'Mark Zuckerberg joins TikTok, Facebook stock plummets'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/news")
def news():
    return render_template('news.html', title='News', articles=articles)

# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful! Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/stocks")
def stocksPage():
    return render_template('stocks.html', title='Stocks', stocks=stocks)

@app.route("/portfolios")
def portfolios():
    return render_template('portfolios.html', title='Portfolios')

@app.route("/groups")
def groups():
    return render_template('groups.html', title='Groups')

@app.route("/stock")
def stockPage():
    return render_template('stock.html', title='AAPL')
