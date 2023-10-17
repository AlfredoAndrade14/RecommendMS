from flask import Flask, jsoninfy, request
app = Flask(__name__)

filmes =[{
'titulo':'Os incriveis',
'genero':'infantil',
'tema':'ação',
'sentimento':'desenho',
},
{
'titulo':'Velozes e furiosos',
'genero':'corrida',
'tema':'ação',
'sentimento':'adrenalina',
},{
'titulo':'Titanic',
'genero':'qualquer idade',
'tema':'romance',
'sentimento':'romance',
}]
@app.route('/filmes')
def get_filmes():
    return jsoninfy(filmes)

app.run(port=8000,host='localhost',debug=True)