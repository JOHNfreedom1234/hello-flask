from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open("diseases.json", "r") as f:
    diseases = json.load(f)

@app.route("/")
def home():
    return render_template({"index.html"})

@app.route("/diagnostic", methods=["POST", "GET"])
def search():
    search_symptoms = []

    if request.method == "GET":
        symptoms = request.args.get("symptoms", "").lower()
        if symptoms:
            search_symptoms = symptoms.split(",")

    elif request.method == "POST":
        search_symptoms = request.json.get("symptoms",[])

    
    matching_diseases = []
    for disease, info in diseases.items():
        synoyms = info.get("Synonyms","").split(";")
        match_symptoms = set(synoyms) & set(search_symptoms)
        if match_symptoms:
            matching_diseases.append({
                "name": disease,
                "match_count": len(match_symptoms),
                "info_link": info.get("info_link_data",[]),
                "icd10_codes": info.get("icd10cm_codes", ""),
            })
    
    matching_diseases.sort(key=lambda x: x["match_count"], reverse=True)
    return jsonify(matching_diseases)

if __name__ == "__main__":
    app.run(debug=True)
