from flask import Flask, render_template


app = Flask(__name__)


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


@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


@app.route('/tovar/<beton>')
def beton_(beton):
    # выбранный бетон
    with open(f'beton/{beton}.txt', encoding='UTF-8') as f:
        info_ = f.read().split('#')
        return render_template('beton.html', info=info_, beton=beton)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
