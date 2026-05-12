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