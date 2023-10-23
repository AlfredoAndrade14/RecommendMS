from flask import Flask, jsonify, request
import openai

app = Flask(__name__)

# Defina a chave de API do GPT-3
openai.api_key = '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'


# Rota para obter a lista de filmes
@app.route('/filmes', methods=['GET'])
def get_filmes():
    return jsonify(filmes)

# Rota para recomendar um filme com base no sentimento e gênero fornecidos pelo usuário
@app.route('/filmes/recomendar', methods=['POST'])
def recomendar_filme():
    data = request.get_json()
    sentimento = data.get('sentimento', 'alegria')
    genero = data.get('genero', 'terror')

    # Usando o GPT-3 para gerar uma recomendação de filme com base no sentimento e gênero
    prompt = f"Recomenda 5 filmes que tenha relacao com meu sentimento de {sentimento} e tenha um gênero {genero}. Quero em portugues"

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
        max_tokens=200, 
        n=1,
        stop=None,
        temperature=0.7
    )

    recommended_movie_text = response.choices[0].text.strip()

    # Divida a string em uma lista de filmes
    recommended_movies_list = [movie.strip() for movie in recommended_movie_text.split('\n') if movie.strip()]

    return jsonify({'recommended_movies': recommended_movies_list})



if __name__ == '__main__':
    app.run(port=8000, host='localhost', debug=True)
