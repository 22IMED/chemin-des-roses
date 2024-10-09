from flask import Flask, request, jsonify
from flask_cors import CORS  # Importez CORS
import joblib

app = Flask(__name__)
CORS(app)  # Activez CORS pour toutes les routes

# Chargez votre modèle ici
model = joblib.load('decision_tree_model.pkl')
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    features = [
        1 if data['Nodule'] == 'oui' else 0,
        1 if data['Douleur'] == 'oui' else 0,
        1 if data['Changement_de_forme'] == 'oui' else 0,
        1 if data['Écoulement'] == 'oui' else 0,
        1 if data['Rougeur'] == 'oui' else 0,
        1 if data['Ganglions'] == 'oui' else 0,
        1 if data['Antécédents_familiaux'] == 'oui' else 0
    ]

    prediction = model.predict([features])  # Faites une prédiction
    if prediction[0] == 1:
        response = 'Recommandation : Visitez un médecin.'
    else:
        response = 'Recommandation : Pas de besoin immédiat de consultation.'

    return jsonify({'prediction': response})

    # return jsonify({'prediction': 'Positif' if prediction[0] == 1 else 'Négatif'})

if __name__ == '__main__':
    app.run(debug=True)
