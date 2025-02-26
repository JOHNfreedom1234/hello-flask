from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv, dotenv_values
from google import genai
from flask_cors import CORS
import json
from pydantic import BaseModel

class Diagnosis (BaseModel)
    key_id: str
    primary_name: str
    consumer_name: str
    word_synonyms: str
    synonyms: list[str]
    info_link_data: list[str]

load_dotenv()

config = dotenv_values(".env")

client = genai.client(api_key=config['GEMINI_API_KEY'])

app = Flask(__name__)
CORS(app)

diseases = []

with open("diseases.json", "r") as f:
    diseases = json.load(f)

@app.route("/")
def home():
    return render_template({"index.html"})

@app.route

@app.route("/diagnostic", methods=["GET"])
def search():
    symptoms = request.args.get('symptoms', '').lower()
    response = client.models.generate_content
    model = "gemini-2.0-flash",
    contents=[
        "This is the existing data in JSON format"
    ]
    

if __name__ == "__main__":
    app.run(debug=True)
