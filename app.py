from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Witaj w cw_praca_z_kodem!'

@app.route('/hello')
def hello():
    # Zamiast "Hello, World!", podaj swoje imię
    return 'Witaj, Mateusz!'

@app.route('/hello/<name>')
def hello_name(name):
    # Ta trasa pozostaje bez zmian, nadal przyjmuje parametr 'name'
    return 'Witaj, {}!'.format(name)

if __name__ == '__main__':
    app.run(debug=True)

