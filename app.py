from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai


app = Flask(__name__)
CORS(app)

def myChat(api_key, prompt):
    #openai.api_key = "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"
    openai.api_key = api_key

    response = openai.Completion.create(
        model = "text-davinci-003", # o mais rapido porem o mais lento
        prompt = prompt,
        max_tokens = 2048,
    )

    return response.choices[0].text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_response():
    try:
        api_key = request.args.get("api_key")
        pergunta = request.args.get("msg")
        resposta = myChat(api_key, pergunta)
    except Exception as e:
        resposta = f"Ops! Ocorreu algum erro :( \n {e}"

    return resposta

app.run()