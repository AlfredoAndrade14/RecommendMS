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
    genero = data.get('genero')
    tema = data.get('tema')
    sentimento = data.get('sentimento')

    prompt = f"Aja como um recomendador de filmes e séries. Recomende 10 filmes ou séries diferentes com os títulos em portugues e enumerados"
    if genero:
        prompt = prompt + f" do gênero {genero}"

    if tema:
        prompt = prompt + f" com o tema {tema}"

    if sentimento:
        prompt = prompt + f" com relacao ao sentimento de {sentimento}"

    print(prompt)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2500,
        n=5,
        stop=None,
        temperature=0.5
    )

    recommended_movie = response.choices[0].text.strip()

    print(recommended_movie)

    return jsonify({'recommended_movie': recommended_movie})

if __name__ == '__main__':
    app.run(port=8000, host='localhost', debug=True)
