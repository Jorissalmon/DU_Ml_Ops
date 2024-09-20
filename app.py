from flask import Flask, render_template, request
import pickle
import pandas as pd
from dotenv import load_dotenv



# Charger les variables d'environnement
load_dotenv()



# Initialiser l'application Flask et charger le modèle
app = Flask(__name__)
model = pickle.load(open("random_forest_model2.pkl", "rb"))

# Fonction pour effectuer une prédiction
def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])

# Page d'accueil
@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")

# Route pour la prédiction
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Extraire les données du formulaire
        credit_lines_outstanding = int(request.form["lignes de crédit en cours"])
        loan_amt_outstanding = int(request.form["montant du prêt en cours"])
        total_debt_outstanding = int(request.form["dette totale en cours"])
        income = float(request.form["revenu"])
        years_employed = int(request.form["années d'emploi"])
        fico_score = int(request.form["score FICO"])

        # Préparer les données pour la prédiction
        features = {
            "credit_lines_outstanding": credit_lines_outstanding,
            "loan_amt_outstanding": loan_amt_outstanding,
            "total_debt_outstanding": total_debt_outstanding,
            "income": income,
            "years_employed": years_employed,
            "fico_score": fico_score,
        }

        # Effectuer la prédiction
        prediction = model_pred(features)

        # Déterminer le texte du résultat
        if prediction == 1:
            prediction_text = "Le client est à risque de défaut de paiement."
        else:
            prediction_text = "Le client n'est pas à risque de défaut de paiement."

        # Enregistrer la prédiction avec Arize
        log_prediction(features, prediction)

        # Renvoyer la page avec le résultat de la prédiction
        return render_template("index.html", prediction_text=prediction_text)
    else:
        return render_template("index.html")

# Exécuter l'application Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
