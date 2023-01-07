from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai


app = Flask(__name__)
CORS(app)

def myChat(prompt):
    openai.api_key = "YOUR-API-KEY-HERE"

    response = openai.Completion.create(
        model = "text-davinci-003", # o mais rapido porem o mais lento
        prompt = prompt,
        max_tokens = 2048,
    )

    return response.choices[0].text


@app.route("/chatbot")

def chatbot():
    try:
        pergunta = request.args.get("pergunta")
        resposta = myChat(pergunta)
    except Exception as e:
        resposta = f"Ops! Ocorreu algum erro :( \n {e}"

    return jsonify(resposta=resposta)


app.run()