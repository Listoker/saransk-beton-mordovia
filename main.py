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
        with open(f'assortiment/{tovar}_spisok.txt', encoding='UTF-8') as k:
            text_vsego = f.read().split('#')
            info = k.read().split('#')
            return render_template('assortiment.html', tovari=text_vsego, infoo=info)


@app.route('/kontakti')
def kontakti():
    # контакты
    return render_template('kontakti.html')


@app.route('/tovar/<beton>')
def beton_(beton):
    # выбранный бетон
    with open(f'beton/{beton}.txt', encoding='UTF-8') as f:
        info_ = f.read().split('#')
        return render_template('beton.html', info=info_, beton=beton)


@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


@app.route('/yandex_c40aeeb4878e9f6b.html')
def yandex():
    return render_template('yandex_c40aeeb4878e9f6b.html')


@app.route('/yandex_33ff5a54adc614ce.html')
def yandexx():
    return render_template('yandex_33ff5a54adc614ce.html')


@app.route('/google2f825bb41dc7f45d.html')
def google():
    return render_template('google2f825bb41dc7f45d.html')


@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.txt')


if __name__ == '__main__':
    app.run(host='0.0.0.0')