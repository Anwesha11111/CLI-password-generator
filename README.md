Password Generator
A command-line password generator written in Python that creates secure, customizable passwords on demand.

🚀 Project Overview
This utility generates random passwords based on user-selected criteria such as length and character type (uppercase, lowercase, digits, symbols). It uses Python's secure secrets module, and is ideal for anyone who needs strong, unique passwords quickly from the terminal.

✨ Features
Interactive command-line prompts

Customizable password length

Choice to include/exclude:

Uppercase letters

Lowercase letters

Digits

Symbols

Secure randomness (secrets module)

📦 Tech Stack
Python 3 (no third-party dependencies)

🛠️ Installation
Clone this repository:

```bash
git clone https://github.com/Anwesha11111/password-generator.git
```
Navigate to the project folder:

```bash
cd password-generator
```
Set up a virtual environment:

```bash
python -m venv venv
# Activate the venv (Windows)
venv\Scripts\activate
# Or activate the venv (macOS/Linux)
source venv/bin/activate
```
No further installation needed. All modules used are built-in.

▶️ Usage:
Run the script, answer prompts for your preferred options, and your secure password will be displayed:

```bash
python generate_password.py
```
Example outputs:

```text
Enter password length: 14
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): n
Include symbols? (y/n): y
Generated password: W&cT!qkdxApzNe
```
💾 File List
```text
password-generator/
├── generate_password.py   # Main script
├── README.md              # Documentation
└── .gitignore             # Ignore Python cache, venv, etc.
```
📂 Sample .gitignore
```text
__pycache__/
*.pyc
venv/
.env
```
📣 Contribution
Contributions are welcome! Fork the repo, create a feature branch, and submit a pull request.

📜 License
MIT License
