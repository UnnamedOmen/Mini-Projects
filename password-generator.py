# collect password criteria
# length
# uppercase
# special characters
# numbers

# get all available characters
# randomly pick characters up to the length
# ensure at least one of each character length
# ensure length is valid (length >= available character types)

import random
import string

def password_generator():
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Would you like to include uppercase? (yes/no) ").strip().lower()
    include_special = input("Would you like to include special characters? (yes/no) ").strip().lower()
    include_digits = input("Would you like to include numbers? (yes/no) ").strip().lower()
    
    if length < 4:
        length = int(input("Password length must be 4 or more. Try again: 3"))
        return length
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + upper + special + digits

    required_characters = []
    if include_uppercase == 'yes':
        required_characters.append(random.choice(upper))
    if include_special == 'yes':
        required_characters.append(random.choice(special))
    if include_digits == 'yes':
        required_characters.append(random.choice(digits))   

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)
    
    random.shuffle(password)

    str_password = "".join(password)
    return str_password

password = password_generator()
print(password)