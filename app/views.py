from flask import render_template
from app import app, models

@app.route('/')
@app.route('/index')
def index():
    datas = models.Zakup.query.all()    
    return render_template("index.html",
        title = 'zakupki',
        datas = datas)