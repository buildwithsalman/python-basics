# Password Strength Checker

A simple Python program that checks the strength of a password based on character types and length.

## Features

- Detects if password is:
  - Too short
  - Weak
  - Moderate
  - Strong
- Checks for:
  - Letters (a–z, A–Z)
  - Numbers (0–9)
  - Special characters (!, @, #, etc.)
- Provides improvement suggestions

## How It Works

The program:
1. Takes a password input from the user.
2. Checks for the presence of:
   - Alphabets (`isalpha()`)
   - Digits (`isdigit()`)
   - Special characters (`not isalnum()`)
3. Analyzes the password length.
4. Prints the strength and suggestions accordingly.