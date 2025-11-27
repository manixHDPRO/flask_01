from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Salut HD PRO ! C\'est ma première application Flask.'

@app.route('/about')
def about():
    return 'À propos de cette application Flask.'

@app.route('/contact')
def contact():
    return 'Ceci est une page de contact.'

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        return 'Vous envoyez des données !'
    else:
        return 'Vous visualisez uniquement le formulaire'

