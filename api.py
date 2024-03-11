from flask import Flask, jsonify
import random

app = Flask(__name__)

# Exemple de données sur les pays
pays = [
    {"nom": "France", "population": 67000000, "capitale": "Paris"},
    {"nom": "Allemagne", "population": 83000000, "capitale": "Berlin"},
    {"nom": "Espagne", "population": 47000000, "capitale": "Madrid"}
]


# Route pour obtenir des données sur les pays
@app.route('/api/pays', methods=['GET'])
def get_pays():
    return jsonify(pays[random.randint(0, len(pays) - 1)])


if __name__ == '__main__':
    app.run(debug=True)
