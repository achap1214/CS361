from flask import render_template, request, url_for, flash, redirect
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm, StockPriceForm
from flaskapp.models import User, Stock
import time

stocks = [
    {
        'symbol': 'AAPL',
        'last': '$162.04',
        'gainLoss': '0.88%'
    },
    {
        'symbol': 'AMZN',
        'last': '$3159.60',
        'gainLoss': '0.47%'
    },
    {
        'symbol': 'BB',
        'last': '$7.00',
        'gainLoss': '2.64%'
    },
    {
        'symbol': 'FB',
        'last': '$212.76',
        'gainLoss': '2.37%'
    },
    {
        'symbol': 'MSFT',
        'last': '$296.99',
        'gainLoss': '0.60%'
    },
    {
        'symbol': 'NVDA',
        'last': '$261.44',
        'gainLoss': '5.56%'
    },
    {
        'symbol': 'TSLA',
        'last': '$894.67',
        'gainLoss': '2.61%'
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

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        if 'stock_symbol' in request.args:
            stock_symbol = request.args['stock_symbol']
            with open('symbolprice.txt', 'w') as f:
                f.write(stock_symbol)
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        with open('symbolprice.txt', 'w') as f:
            f.write(stock_symbol)
        time.sleep(5)
        with open('symbolprice.txt', 'r') as f:
            price = f.read()
        clear = open('symbolprice.txt', 'w')
        clear.close()
        return price
    return render_template('home.html')

@app.route("/news")
def news():
    return render_template('news.html', title='News', articles=articles)

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
