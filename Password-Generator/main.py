import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the PyPassword Generator!")
letter = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you like?\n"))
number = int(input("How many numbers would you like?\n"))

# Create lists for each category with the desired counts
password_letters = random.choices(letters, k=letter)
password_symbols = random.choices(symbols, k=symbol)
password_numbers = random.choices(numbers, k=number)

# Concatenate the generated lists into a single password
password = password_letters + password_symbols + password_numbers
random.shuffle(password)
generated_password = "".join(password)

print("Generated password:", generated_password)


