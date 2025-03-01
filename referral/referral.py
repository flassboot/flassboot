
import sqlite3
import random
import string

# Database setup for referral system
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS referrals (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        code TEXT UNIQUE,
        invites INTEGER DEFAULT 0,
        discount REAL DEFAULT 0.0,
        free_months INTEGER DEFAULT 0
    )
''')
conn.commit()

# Function to generate unique referral code
def generate_referral_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Function to create a referral code for a user
def create_referral_code(user_id):
    code = generate_referral_code()
    try:
        cursor.execute("INSERT INTO referrals (user_id, code) VALUES (?, ?)", (user_id, code))
        conn.commit()
        return code
    except sqlite3.IntegrityError:
        return create_referral_code(user_id)

# Function to handle a referral
def use_referral_code(code):
    cursor.execute("SELECT * FROM referrals WHERE code = ?", (code,))
    referral = cursor.fetchone()
    if referral:
        new_invites = referral[3] + 1
        free_months = referral[5]
        discount = referral[4]

        # Aplică luna gratuită la fiecare 5 invitați
        if new_invites % 5 == 0:
            free_months += 1
            discount = 0.0  # Anulează discount-ul dacă se primește lună gratuită
        else:
            discount = min(15.0, new_invites * 5.0)  # Max 15% discount dacă nu e luna gratuită

        cursor.execute("UPDATE referrals SET invites = ?, discount = ?, free_months = ? WHERE code = ?",
                       (new_invites, discount, free_months, code))
        conn.commit()
        return {"discount": discount, "free_months": free_months}
    return {"discount": 0, "free_months": 0}

# Function to get referral details
def get_referral_info(user_id):
    cursor.execute("SELECT * FROM referrals WHERE user_id = ?", (user_id,))
    return cursor.fetchone()

# Example usage
if __name__ == '__main__':
    user_id = 1  # Example user ID
    code = create_referral_code(user_id)
    print(f'Referral Code for User {user_id}: {code}')
    print('Applying referral code...')
    print(f'Benefits Applied: {use_referral_code(code)}')
    print(f'Referral Info: {get_referral_info(user_id)}')
