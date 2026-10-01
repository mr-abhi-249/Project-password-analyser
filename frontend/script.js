const passwordInput = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");
const analyzeBtn = document.getElementById("analyzeBtn");
const result = document.getElementById("result");


// Show / Hide Password
togglePassword.addEventListener("click", () => {
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePassword.textContent = "Hide";
    } else {
        passwordInput.type = "password";
        togglePassword.textContent = "Show";
    }
});


// Analyze when button is clicked
analyzeBtn.addEventListener("click", analyzePassword);


// Analyze when Enter key is pressed
passwordInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        analyzePassword();
    }
});


// Send password to Flask backend
async function analyzePassword() {

    const password = passwordInput.value;

    if (!password) {
        alert("Please enter a password.");
        return;
    }

    try {

        const response = await fetch("/api/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                password: password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.error || "Something went wrong.");
            return;
        }

        displayResult(data);

    } catch (error) {

        alert("Unable to connect to the server.");

        console.error(error);
    }
}


// Display analysis result
function displayResult(data) {

    result.classList.remove("hidden");

    document.getElementById("strengthText").textContent =
        `Strength: ${data.strength}`;

    updateCheck("length", data.length >= 8);
    updateCheck("uppercase", data.uppercase);
    updateCheck("lowercase", data.lowercase);
    updateCheck("number", data.number);
    updateCheck("special", data.special);
    updateCheck("common", !data.common);
    updateCheck("predictable", !data.predictable);
    updateCheck("repeated", !data.repeated);


    // Update strength bar
    const strengthFill = document.getElementById("strengthFill");

    if (data.strength === "Weak") {
        strengthFill.style.width = "33%";
    } else if (data.strength === "Medium") {
        strengthFill.style.width = "66%";
    } else {
        strengthFill.style.width = "100%";
    }


    // Display suggestions
    const suggestionList = document.getElementById("suggestionList");

    suggestionList.innerHTML = "";

    if (data.suggestions.length === 0) {

        const li = document.createElement("li");
        li.textContent = "Your password meets all current checks.";
        suggestionList.appendChild(li);

    } else {

        data.suggestions.forEach(suggestion => {

            const li = document.createElement("li");
            li.textContent = suggestion;

            suggestionList.appendChild(li);
        });
    }
}


// Update security checklist
function updateCheck(id, passed) {

    const element = document.getElementById(id);

    if (passed) {
        element.textContent =
            element.textContent.replace("❌", "✅");
    } else {
        element.textContent =
            element.textContent.replace("✅", "❌");
    }
}