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

    budget = int(data['budget'])

    diet = data['diet']

    # Validation

    if calories < 1000 or calories > 5000:

        return jsonify({

            "error":
            "Calories must be between 1000 and 5000"

        }), 400

    if budget < 50 or budget > 5000:

        return jsonify({

            "error":
            "Budget must be between ₹50 and ₹5000"

        }), 400

    # ML Recommendation

    meals = recommend_meals(calories, diet)

    return jsonify(meals)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)