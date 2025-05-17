import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    all_chars = letters + digits + punctuation
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(punctuation)
    ]
    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)
    return ''.join(password)

print("Generated Password:", generate_password(12))