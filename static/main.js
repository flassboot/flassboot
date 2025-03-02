
// main.js - Script principal pentru FlassTradingBoot (Actualizat)

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
    localStorage.setItem("theme", theme.toLowerCase());
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

// Funcție pentru a gestiona notificările
function showNotification(message, type = "info") {
    const notification = document.createElement("div");
    notification.className = `notification ${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Adăugare funcționalitate de live chat
function sendMessage() {
    const messageInput = document.getElementById("chatInput");
    const message = messageInput.value.trim();
    if (message) {
        // Afișează mesajul în chat
        const chatBox = document.getElementById("chatBox");
        const userMessage = document.createElement("div");
        userMessage.className = "chat-message user";
        userMessage.textContent = message;
        chatBox.appendChild(userMessage);
        messageInput.value = "";

        // Simulare răspuns de la bot
        setTimeout(() => {
            const botMessage = document.createElement("div");
            botMessage.className = "chat-message bot";
            botMessage.textContent = "This is a simulated response from FlassBot!";
            chatBox.appendChild(botMessage);
        }, 1000);
    }
}

// Funcție pentru a extinde și restrânge secțiunile de pe pagină
function toggleSection(sectionId) {
    const section = document.getElementById(sectionId);
    section.classList.toggle("collapsed");
}

// Funcție pentru a actualiza datele afișate pe dashboard
function updateDashboard() {
    fetch("/api/dashboard")
        .then(response => response.json())
        .then(data => {
            document.getElementById("totalTrades").innerText = data.total_trades;
            document.getElementById("profitLoss").innerText = `${data.profit_loss}%`;
        })
        .catch(error => console.error("Error updating dashboard:", error));
}

// Actualizează dashboard la fiecare 30 de secunde
setInterval(updateDashboard, 30000);
