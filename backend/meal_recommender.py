import pandas as pd

# Load dataset
df = pd.read_csv('../dataset/curated_meals.csv')

def recommend_meals(calories_needed, diet_type):

    # Filter by diet
    if diet_type == 'Both':
        filtered = df
    else:
        filtered = df[
            df['diet'] == diet_type
        ]

    # Sort by protein
    filtered = filtered.sort_values(
        by='protein',
        ascending=False
    )

    # Separate meal categories
    breakfast_df = filtered[
        filtered['meal_type'] == 'Breakfast'
    ]

    lunch_df = filtered[
        filtered['meal_type'] == 'Lunch'
    ]

    dinner_df = filtered[
        filtered['meal_type'] == 'Dinner'
    ]

    snacks_df = filtered[
        filtered['meal_type'] == 'Snacks'
    ]

    # Random meal selection
    breakfast = breakfast_df.sample(1).iloc[0]
    lunch = lunch_df.sample(1).iloc[0]
    dinner = dinner_df.sample(1).iloc[0]
    snacks = snacks_df.sample(1).iloc[0]

    result = {

        "breakfast":
        breakfast['meal_name'],

        "lunch":
        lunch['meal_name'],

        "dinner":
        dinner['meal_name'],

        "snacks":
        snacks['meal_name']
    }

    return result