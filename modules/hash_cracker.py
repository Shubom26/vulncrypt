import os
import hashlib
from termcolor import colored
import time
import pyfiglet

def show_banner():
    banner = pyfiglet.figlet_format("Hash Cracker")
    print(colored(banner, "cyan", attrs=["bold"]))
   

def load_wordlist():
    # Fix: use _file_ with double underscores
    path = os.path.join(os.path.dirname(__file__), "wordlists", "rockyou.txt")
    passwords = []
    try:
        with open(path, "r", encoding="latin-1") as file:
            passwords = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(colored("Error: rockyou.txt wordlist file not found.", "red"))
    return passwords

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

def hash_cracker_cli():
    show_banner()
    print(colored("Welcome to the Hash Password Cracker!\n", "yellow"))

    hash_value = input(colored("Enter the hashed password: ", "green")).strip()
    hash_type = input(colored("Enter hash type (md5, sha1, sha256, sha512): ", "green")).strip().lower()

    hash_func = get_hash_function(hash_type)
    if not hash_func:
        print(colored("Unsupported hash type! Returning to main menu.", "red"))
        time.sleep(2)
        return

    passwords = load_wordlist()
    if not passwords:
        print(colored("No passwords loaded. Cannot proceed.", "red"))
        time.sleep(2)
        return

    print(colored(f"\nLoaded {len(passwords)} passwords. Starting crack...\n", "yellow"))

    start_time = time.time()
    for idx, pw in enumerate(passwords, 1):
        hashed_pw = hash_func(pw.encode()).hexdigest()
        if hashed_pw == hash_value:
            elapsed = time.time() - start_time
            print(colored(f"\nPassword found: '{pw}'", "green"))
            print(colored(f"Time taken: {elapsed:.2f} seconds\n", "green"))
            input(colored("Press Enter to return to main menu...", "yellow"))
            return
        if idx % 100000 == 0:
            print(colored(f"Tried {idx} passwords so far...", "blue"))

    print(colored("\nPassword not found in wordlist.", "red"))
    input(colored("Press Enter to return to main menu...", "yellow"))

if __name__ == "__main__":
    hash_cracker_cli()
