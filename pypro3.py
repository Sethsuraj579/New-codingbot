import random # for generating random numbers
import string # for string operations

def generate_password(length): # functions to generator password
    if length < 4:  # Ensure minimum length for a secure password
          print("Password length must be at least 4 characters.")
          return None
    elif length > 20: # Ensure maximum length for a secure password
            print("Password length must be at most 20 characters.")
            return None
    else:
            print("Passwird length is valid.")
            # Define character pools
            lower = string.ascii_lowercase # lowercase letters
            upper = string.ascii_uppercase # uppercase letters
            digits = string.digits # digits 0-9
            symbols = string.punctuation # soecial charactors

            # Ensure the password contains at least one of each type
            all_characters = lower + upper + digits + symbols
            password = [
              random.choice(lower),
              random.choice(upper),
              random.choice(digits),
              random.choice(symbols)
         ] # start with one of each charactor

          # Fill the rest of the password length with random choices
            password += random.choices(all_characters, k=length - 4)

          # Shuffle the password to avoid predictable patterns
            random.shuffle(password)
            return ''.join(password)

# Example usage a secure password 
length = int(input("Enter the desired password length: "))
print("Generated password:", generate_password(length))