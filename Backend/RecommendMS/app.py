from flask import Flask, jsonify, request

app = Flask(__name)

filmes = [
    {
        'titulo': 'Os Incríveis',
        'genero': 'Infantil',
        'tema': 'Ação',
        'sentimento': 'Desenho',
    },
    {
        'titulo': 'Velozes e Furiosos',
        'genero': 'Corrida',
        'tema': 'Ação',
        'sentimento': 'Adrenalina',
    },
    {
        'titulo': 'Titanic',
        'genero': 'Qualquer Idade',
        'tema': 'Romance',
        'sentimento': 'Romance',
    }
]

@app.route('/filmes')
def get_filmes():
    return jsonify(filmes)

if __name__ == '__main__':
    app.run(port=8000, host='localhost', debug=True)
