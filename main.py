import os
import datetime
from flask import Flask, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired
from data import db_session
import sqlalchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class MyForm(FlaskForm):
    name = FloatField('A', validators=[InputRequired()])

@app.route('/')
def glavnoe():
    # главное окно
    return render_template('glavnoe.html')


@app.route('/assortiment/<tovar>')
def assortiment(tovar):
    # ассортимент
    with open(f'assortiment/{tovar}.txt', encoding='UTF-8') as f:
        text_vsego = f.read().split('#')
        return render_template('assortiment.html', tovari=text_vsego)


@app.route('/kontakti')
def kontakti():
    # контакты
    return render_template('kontakti.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        print(name)
        return render_template('calculator.html', form=form)
    return render_template('calculator.html', form=form)


@app.route('/tovar/<beton>')
def beton_(beton):
    # выбранный бетон
    with open(f'beton/{beton}.txt', encoding='UTF-8') as f:
        info_ = f.read().split('#')
        return render_template('beton.html', info=info_, beton=beton)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
