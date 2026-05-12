const mealForm = document.getElementById("mealForm");

if (mealForm) {

    mealForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        // Collect form data
        const data = {

            diet: document.getElementById("diet").value,

            goal: document.getElementById("goal").value,

            budget: document.getElementById("budget").value,

            calories: document.getElementById("calories").value

        };
const calories = parseInt(data.calories);

const budget = parseInt(data.budget);

// Calories validation
if (calories < 1000 || calories > 5000) {

    alert(
        "Please enter calories between 1000 and 5000."
    );

    return;
}

// Budget validation
if (budget < 50 || budget > 5000) {

    alert(
        "Please enter budget between ₹50 and ₹5000."
    );

    return;
}
        try {

            // Send data to Flask backend
            const response = await fetch(
                "http://127.0.0.1:5000/generate_meal",
                {

                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(data)

                }
            );

            // Convert response to JSON
            const result = await response.json();

            console.log(result);

            // Save result in local storage
            localStorage.setItem(
                "mealPlan",
                JSON.stringify(result)
            );

            // Redirect to dashboard
            window.location.href = "dashboard.html";

        }

        catch (error) {

            console.error(error);

            alert("Error connecting to backend!");

        }

    });

}