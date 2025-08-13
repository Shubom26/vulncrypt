#!/home/kali/vulncrypt/venv/bin/python3

import random
import string
import time
import os
import pyfiglet
from termcolor import colored

def print_separator():
    print(colored("=" * 60, "cyan"))

def show_banner():
    os.system("clear")
    banner = pyfiglet.figlet_format("Password Suggestions")
    print(colored(banner, "cyan", attrs=["bold"]))

def loading_animation(message="Generating password"):
    print(colored(message, "yellow"), end="")
    for _ in range(3):
        print(colored(".", "yellow"), end="", flush=True)
        time.sleep(0.5)
    print()

def yes_no_prompt(prompt):
    while True:
        choice = input(colored(prompt + " (y/n): ", "yellow")).strip().lower()
        if choice in ("y", "n"):
            return choice == "y"
        else:
            print(colored("Please enter 'y' or 'n'.", "red"))

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pools = []
    if use_upper:
        char_pools.append(string.ascii_uppercase)
    if use_lower:
        char_pools.append(string.ascii_lowercase)
    if use_digits:
        char_pools.append(string.digits)
    if use_symbols:
        char_pools.append("!@#$%^&*()-_=+[]{};:,.<>?")

    if not char_pools:
        return None  # No char sets selected

    all_chars = "".join(char_pools)

    # Ensure password contains at least one char from each selected pool
    password = [random.choice(pool) for pool in char_pools]

    # Fill the rest randomly
    if length < len(password):
        length = len(password)  # minimum length equals number of pools selected

    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

def password_suggestions_cli():
    show_banner()
    print_separator()
    print(colored("   Dynamic Password Suggestions", "cyan", attrs=["bold"]))
    print_separator()

    while True:
        print(colored("\nSelect character types to include:", "magenta"))
        use_upper = yes_no_prompt("Include UPPERCASE letters?")
        use_lower = yes_no_prompt("Include lowercase letters?")
        use_digits = yes_no_prompt("Include numbers?")
        use_symbols = yes_no_prompt("Include symbols?")

        if not (use_upper or use_lower or use_digits or use_symbols):
            print(colored("Error: You must select at least one character type.", "red"))
            continue

        try:
            length_input = input(colored("Enter desired password length (min 8): ", "yellow")).strip()
            length = int(length_input)
            if length < 8:
                print(colored("Length too short, setting to 8.", "red"))
                length = 8
        except ValueError:
            print(colored("Invalid input. Please enter a number.", "red"))
            continue

        loading_animation()

        pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        if pwd is None:
            print(colored("Password generation failed due to invalid character set selection.", "red"))
            continue

        print_separator()
        print(colored("Suggested Password:", "green", attrs=["bold"]))
        print(colored(pwd, "blue", attrs=["bold"]))
        print_separator()

        again = input(colored("Generate another password? (y/n): ", "yellow")).strip().lower()
        if again != "y":
            print(colored("\nReturning to main menu...\n", "magenta"))
            break

if __name__ == "__main__":
    password_suggestions_cli()

