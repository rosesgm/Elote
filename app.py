from flask import Flask, render_template, request
from entities.palindrome import Palindrome

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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
