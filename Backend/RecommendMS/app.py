from flask import Flask, jsonify, request

app = Flask(__name__)

filmes = [
    {
        'titulo': 'Os Incriveis',
        'genero': 'Infantil',
        'tema': 'Acao',
        'sentimento': 'Desenho',
    },
    {
        'titulo': 'Velozes e Furiosos',
        'genero': 'Corrida',
        'tema': 'Acao',
        'sentimento': 'Adrenalina',
    },
    {
        'titulo': 'Titanic',
        'genero': 'Qualquer Idade',
        'tema': 'Romance',
        'sentimento': 'Romance',
    }
]

@app.route('/filmes', methods={'GET'})
def getAll_filmes():
    return jsonify(filmes)

@app.route('/filmes/titulo/<string:titulo>', methods={'GET'})
def getFilmesByTitulo(titulo):
    for filme in filmes:
        if filme.get('titulo').upper() == titulo.upper():
            return jsonify(filme)
        
@app.route('/filmes/genero/<string:genero>', methods={'GET'})
def getAllFilmesByGenero(genero):
    filmesTemp=[]
    for filme in filmes:
        if filme.get('genero').upper() == genero.upper():
            filmesTemp.append(filme)
    return jsonify(filmesTemp)
        
@app.route('/filmes/tema/<string:tema>', methods={'GET'})
def getAllFilmesByTema(tema):
    filmesTemp=[]
    for filme in filmes:
        if filme.get('tema').upper() == tema.upper() or filme.get('sentimento').upper() == tema.upper():
            filmesTemp.append(filme)
    return jsonify(filmesTemp)




if __name__ == '__main__':
    app.run(port=8000, host='localhost', debug=True)
