
import sqlite3
import random
import string

# Funcție pentru a genera un cod de referință unic
def generate_referral_code(username):
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{username[:3].upper()}-{random_part}"

# Funcție pentru a salva codul de referință în baza de date
def save_referral_code(username, referral_code):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET referral_code = ? WHERE username = ?", (referral_code, username))
    conn.commit()
    conn.close()

# Funcție pentru a valida codul de referință
def validate_referral_code(referral_code):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE referral_code = ?", (referral_code,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Funcție pentru a gestiona bonusul pentru invitații aduși
def handle_referral_bonus(referral_code):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Verificăm dacă codul de referință este valid
    cursor.execute("SELECT username FROM users WHERE referral_code = ?", (referral_code,))
    user = cursor.fetchone()
    if user:
        username = user[0]
        # Incrementăm numărul de invitați
        cursor.execute("UPDATE users SET invites = invites + 1 WHERE username = ?", (username,))
        conn.commit()

        # Verificăm dacă utilizatorul a adus 5 invitați
        cursor.execute("SELECT invites FROM users WHERE username = ?", (username,))
        invites = cursor.fetchone()[0]
        if invites >= 5:
            # Activăm 1 lună gratuită
            cursor.execute("UPDATE users SET subscription_active = 1, trial_end = date('now', '+30 days') WHERE username = ?", (username,))
            conn.commit()
            print(f"✅ {username} has earned 1 month free subscription!")

    conn.close()
