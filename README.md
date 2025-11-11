# CLI-password-generator
A CLI tool to quickly generate secure passwords with custom options.
Password Generator
A command-line password generator written in Python. Quickly generate secure, customizable passwords with options for length, symbols, numbers, and case.

Features
Choose password length

Include/exclude uppercase, lowercase, digits, and symbols

Simple and secure (uses Python's secrets module)

Outputs password directly to your terminal

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/password-generator.git
Navigate to the project folder:

bash
cd password-generator
(Optional) Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
(For small scripts, this is optional, but good practice.)

No additional libraries required (uses built-in Python modules)

Usage
Run the script and follow the prompts:

bash
python generate_password.py
You'll be asked for:

Password length

Whether to include uppercase, lowercase, numbers, symbols

Example interaction:

text
Enter password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include symbols? (y/n): n
Generated password: g3JpC2aBsR9k
File Structure

.gitignore:
__pycache__/
*.pyc
venv/
.env
License
MIT License
