from flask import Flask, jsonify, request
import openai
from flask_cors import CORS  
 
app = Flask(__name__)
CORS(app)



openai.api_key = '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'



@app.route('/filmes', methods=['GET'])
def get_filmes():
    return jsonify(filmes)


@app.route('/filmes/recomendar', methods=['POST'])
def recomendar_filme():
    data = request.get_json()
    sentimento = data.get('sentimento', 'alegria')
    genero = data.get('genero', 'terror')

  
    prompt = f"Haja como um recomendador de filmes e recomende 5 filmes que tenha relacao com meu sentimento de {sentimento} e tenha um gênero {genero}. Com os títulos em portugues"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=5,
        stop=None,
        temperature=0.7
    )

    recommended_movie = response.choices[0].text.strip()

    print(recommended_movie)

    return jsonify({'recommended_movie': recommended_movie})


@app.route('/filmes/recomendar/nova', methods=['POST'])
def recomendar_filme_nova():
    data = request.get_json()
    sentimento = data.get('sentimento', 'alegria')
    genero = data.get('genero', 'terror')

    prompt = f"Estou com um sentimento {sentimento} e querendo assistir um filme de gênero {genero}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300, 
        n=1,
        stop=None,
        temperature=0.7
    )

    recommended_movie_text = response.choices[0].text.strip()

    # Divida a string em uma lista de filmes
    recommended_movies_list = [movie.strip() for movie in recommended_movie_text.split('\n') if movie.strip()]

    return jsonify({ recommended_movies_list})



if __name__ == '__main__':
    app.run(port=8000, host='localhost', debug=True)
