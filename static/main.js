
// main.js - Script principal pentru FlassTradingBoot

// Afișează un mesaj de bun venit în consola browser-ului
console.log("Welcome to FlassTradingBoot!");

// Funcție pentru a gestiona butoanele de control ale botului
function controlBot(action) {
    fetch(`/${action}`)
        .then(response => response.json())
        .then(data => {
            alert(data.status);
            console.log(data);
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while communicating with the bot.");
        });
}

// Funcție pentru a copia codul de referință în clipboard
function copyReferralCode() {
    const referralCode = document.getElementById("referralCode");
    navigator.clipboard.writeText(referralCode.innerText).then(() => {
        alert("Referral code copied to clipboard!");
    }).catch(err => {
        console.error("Failed to copy: ", err);
    });
}

// Funcție pentru a schimba tema site-ului
function toggleTheme() {
    const body = document.body;
    body.classList.toggle("dark-theme");
    const theme = body.classList.contains("dark-theme") ? "Dark" : "Light";
    alert(`${theme} theme activated!`);
}

// Funcție pentru validarea formularelor
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (form.checkValidity()) {
        return true;
    } else {
        alert("Please fill out all required fields correctly.");
        return false;
    }
}

// Execută funcția de schimbare a temei dacă este salvată în localStorage
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        document.body.classList.add("dark-theme");
    }
});
