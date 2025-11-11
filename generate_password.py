import string
import secrets
length = int(input("Enter password length: "))
include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
charset = ''
if include_upper:
    charset += string.ascii_uppercase
if include_lower:
    charset += string.ascii_lowercase
if include_digits:
    charset += string.digits
if include_symbols:
    charset += string.punctuation
password = ''.join(secrets.choice(charset) for _ in range(length))
print("Generated password:", password)
