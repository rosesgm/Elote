from flask import Flask, render_template, request
from entities.palindrome import Palindrome
from entities.currency import Currency
from entities.animal import Animal
from entities.sorteo import Sorteo

app = Flask(__name__)
# Esta sera la ruta index (de la pagina principal)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/math')
def math():
    return render_template('math.html')


@app.route('/azulejos')
def azulejos():
    return render_template('azulejos.html')


@app.route('/palindrome', methods=['GET', 'POST'])
def palindrome():
    if request.method == 'POST':
        phrase = request.form.get('input_phrase', '')

        p = Palindrome(phrase)
        result = p.is_palindrome()
        return render_template('result.html', resultado=result)
    return render_template('palindrome.html')


@app.route('/currency', methods=['GET', 'POST'])
def currency():
    if request.method == 'POST':
        pesos = request.form.get('input_pesos')
        c = Currency(pesos)
        result = c.to_dollars()
        return render_template('resultado.html', resultado=result)
    return render_template('currency.html')


@app.route('/animals')
def animals():
    return render_template('animals.html', animals=Animal.get_list())


@app.route('/sorteo', methods=['GET', 'POST'])
def sorteo():
    if request.method == 'POST':
        numero1 = request.form.get('input_num1', '')
        numero2 = request.form.get('input_num2', '')
        numero3 = request.form.get('input_num3', '')

        num = Sorteo(numero1, numero2, numero3)
        result = num.ganador()
        return render_template('result_sorteo.html', resultado=result)
    return render_template('sorteo.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
