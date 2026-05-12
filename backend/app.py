from flask import Flask, request, jsonify
from flask_cors import CORS

from meal_recommender import recommend_meals

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return "NutriGenie Backend Running!"


@app.route('/generate_meal', methods=['POST'])
def generate_meal():

    data = request.json

    calories = int(data['calories'])

    diet = data['diet']

    meals = recommend_meals(calories, diet)

    return jsonify(meals)


if __name__ == '__main__':
    app.run(debug=True)