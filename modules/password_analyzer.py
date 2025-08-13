#!/home/kali/vulncrypt/venv/bin/python3

import re
import time
from termcolor import colored
import os
import pyfiglet

def print_separator():
    print(colored("=" * 60, "cyan"))

def show_banner():
    os.system("clear")
    banner = pyfiglet.figlet_format("Password Analyzer")
    print(colored(banner, "cyan", attrs=["bold"]))

def loading_animation():
    print(colored("Analyzing password", "yellow"), end="")
    for _ in range(3):
        print(colored(".", "yellow"), end="", flush=True)
        time.sleep(0.5)
    print()  # newline

def analyze_password(password):
    length = len(password)
    score = 0

    charset_size = 0
    if re.search(r"[a-z]", password):
        charset_size += 26
        score += 1
    if re.search(r"[A-Z]", password):
        charset_size += 26
        score += 1
    if re.search(r"\d", password):
        charset_size += 10
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset_size += 32
        score += 1

    if length >= 8:
        score += 2
    if length >= 12:
        score += 2
    if length >= 16:
        score += 2

    if re.search(r"(.)\1{2,}", password):
        score -= 2
    for seq in ["1234", "abcd", "password", "qwerty", "1111", "0000"]:
        if seq in password.lower():
            score -= 2
            break

    score = max(0, min(10, score))

    if charset_size == 0:
        charset_size = 1

    total_combinations = charset_size ** length
    guesses_per_second = 10_000_000_000
    seconds = total_combinations / guesses_per_second

    if seconds < 60:
        crack_time = f"{seconds:.2f} seconds"
    elif seconds < 3600:
        crack_time = f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        crack_time = f"{seconds/3600:.2f} hours"
    elif seconds < 31_536_000:
        crack_time = f"{seconds/86400:.2f} days"
    elif seconds < 3.154e9:
        crack_time = f"{seconds/31_536_000:.2f} years"
    else:
        crack_time = f"{seconds/(31_536_000*1000):.2f} millennia"

    if score <= 2:
        strength = colored("Very Weak", "red", attrs=["bold"])
    elif score <= 4:
        strength = colored("Weak", "red")
    elif score <= 6:
        strength = colored("Medium", "yellow")
    elif score <= 8:
        strength = colored("Strong", "green")
    else:
        strength = colored("Very Strong", "green", attrs=["bold"])

    return score, strength, crack_time

def password_analyzer_cli():
    show_banner()
    print_separator()
    print(colored("Welcome to the Password Strength Analyzer\n", "cyan", attrs=["bold"]))
    print(colored("Password Requirements Reminder:", "magenta", attrs=["underline"]))
    print(colored("- Use at least 8 characters", "magenta"))
    print(colored("- Include lowercase, uppercase, numbers & symbols", "magenta"))
    print(colored("- Avoid common patterns like '1234', 'password', etc.\n", "magenta"))
    print_separator()

    while True:
        pw = input(colored("Enter password to analyze (or press Enter to return to main menu): ", "yellow")).strip()
        if not pw:
            print(colored("\nReturning to main menu...\n", "magenta"))
            break

        loading_animation()

        score, strength, crack_time = analyze_password(pw)

        print_separator()
        print(colored(f"Password: {pw}", "blue", attrs=["bold"]))
        print(colored(f"Score: {score}/10", "blue"))
        print(f"Strength: {strength}")
        print(colored(f"Estimated crack time: {crack_time}", "green"))
        print_separator()

if __name__ == "__main__":
    password_analyzer_cli()
