import pandas as pd

from sklearn.neighbors import NearestNeighbors

from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('../dataset/curated_meals.csv')

# Features used for ML
features = df[['calories', 'protein', 'carbs', 'budget']]

# Scale features
scaler = StandardScaler()

scaled_features = scaler.fit_transform(features)

# Train KNN Model
model = NearestNeighbors(
    n_neighbors=5,
    metric='euclidean'
)

model.fit(scaled_features)

# Recommendation Function
def recommend_meals(calories_needed, diet_type):

    # User input vector
    user_input = [[
        calories_needed,
        25,   # protein target
        50,   # carbs target
        100   # budget target
    ]]

    # Scale input
    scaled_input = scaler.transform(user_input)

    # Find nearest meals
    distances, indices = model.kneighbors(scaled_input)

    # Get recommended meals
    recommended = df.iloc[indices[0]]

    # Filter by diet
    if diet_type != 'Both':

        recommended = recommended[
            recommended['diet'] == diet_type
        ]

    # Meal categories
    breakfast_df = recommended[
        recommended['meal_type'] == 'Breakfast'
    ]

    lunch_df = recommended[
        recommended['meal_type'] == 'Lunch'
    ]

    dinner_df = recommended[
        recommended['meal_type'] == 'Dinner'
    ]

    snacks_df = recommended[
        recommended['meal_type'] == 'Snacks'
    ]

    result = {

        "breakfast":
        breakfast_df.iloc[0]['meal_name']
        if not breakfast_df.empty
        else "Healthy Breakfast",

        "lunch":
        lunch_df.iloc[0]['meal_name']
        if not lunch_df.empty
        else "Healthy Lunch",

        "dinner":
        dinner_df.iloc[0]['meal_name']
        if not dinner_df.empty
        else "Healthy Dinner",

        "snacks":
        snacks_df.iloc[0]['meal_name']
        if not snacks_df.empty
        else "Healthy Snack"
    }

    return result