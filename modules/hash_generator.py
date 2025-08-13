#!/home/kali/vulncrypt/venv/bin/python3

import hashlib
import pyfiglet
from termcolor import colored
import time
import os

def print_separator():
    print(colored("=" * 60, "cyan"))

def show_banner():
    os.system("clear")
    banner = pyfiglet.figlet_format("Hash Generator")
    print(colored(banner, "cyan", attrs=["bold"]))

def loading_animation(message="Hashing"):
    print(colored(message, "yellow"), end="", flush=True)
    for _ in range(3):
        print(colored(".", "yellow"), end="", flush=True)
        time.sleep(0.5)
    print()

def get_hash_function(hash_type):
    hash_type = hash_type.lower()
    if hash_type == "md5":
        return hashlib.md5
    elif hash_type == "sha1":
        return hashlib.sha1
    elif hash_type == "sha256":
        return hashlib.sha256
    elif hash_type == "sha512":
        return hashlib.sha512
    else:
        return None

def hash_generator_cli():
    show_banner()
    print_separator()
    print(colored("Welcome to the Hash Generator!\n", "cyan", attrs=["bold"]))
    print_separator()

    while True:
        text = input(colored("Enter text to hash (or 'q' to quit): ", "yellow")).strip()
        if text.lower() == 'q':
            print(colored("\nReturning to main menu...\n", "magenta"))
            time.sleep(1)
            break
        if not text:
            print(colored("Input cannot be empty!", "red"))
            continue

        hash_type = input(colored("Enter hash type (md5, sha1, sha256, sha512): ", "yellow")).strip().lower()
        hash_func = get_hash_function(hash_type)

        if not hash_func:
            print(colored("Unsupported hash type! Please try again.", "red"))
            continue

        loading_animation("Generating hash")

        hashed_text = hash_func(text.encode()).hexdigest()
        print_separator()
        print(colored(f"{hash_type.upper()} hash of '{text}':", "yellow", attrs=["bold"]))
        print(colored(hashed_text, "green"))
        print_separator()
        time.sleep(1)

if __name__ == "__main__":
    hash_generator_cli()
