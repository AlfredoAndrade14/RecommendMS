from flask import Flask, jsonify, request
from jinja2 import FileSystemBytecodeCache
import openai

app = Flask(__name__)

# Defina a chave de API do GPT-3
openai.api_key = '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'


# Rota para obter a lista de filmes
@app.route('/filmes', methods=['GET'])
def get_filmes():
    return jsonify(FileSystemBytecodeCache)

# Rota para recomendar um filme com base no sentimento e gênero fornecidos pelo usuário
@app.route('/filmes/recomendar', methods=['POST'])
def recomendar_filme():
    data = request.get_json()
    sentimento = data.get('sentimento', 'alegria')
    genero = data.get('genero', 'terror')

    # Usando o GPT-3 para gerar uma recomendação de filme com base no sentimento e gênero
    prompt = f"Recomendar um filme com sentimento {sentimento} e gênero {genero}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    recommended_movie = response.choices[0].text.strip()

    return jsonify({'recommended_movie': recommended_movie})

if __name__ == '_main_':
    app.run(port=8000, host='localhost', debug=True)