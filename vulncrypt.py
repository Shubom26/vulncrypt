#!/home/kali/vulncrypt/venv/bin/python3

import sys
import time
import os
import pyfiglet
from termcolor import colored

from modules import password_analyzer, password_suggestions, hash_cracker, hash_generator, website_scanner, documentation



def print_separator():
    print(colored("=" * 60, "cyan"))

def show_banner():
    os.system("clear")
    banner = pyfiglet.figlet_format("VulnCrypt")
    print(colored(banner, "cyan", attrs=["bold"]))
    print(colored("Created by: Y Kabir Singha & Shubom Deb\n", "yellow", attrs=["bold"]))
    print(colored("A Professional CLI Security Toolkit\n", "green"))

def main_menu():
    print_separator()
    print(colored(" Main Menu ", "white", "on_blue", attrs=["bold"]))
    print_separator()
    print(colored("[1] Password Strength Analyzer", "blue"))
    print(colored("[2] Password Suggestions", "blue"))
    print(colored("[3] Hash Generator", "blue"))
    print(colored("[4] Hash Password Cracker", "blue"))
    print(colored("[5] Website Vulnerability Scanner", "blue"))
    print(colored("[6] Documentation", "blue"))
    print(colored("[0] Exit", "red"))
    print_separator()



def main():
    show_banner()
    while True:
        main_menu()
        choice = input(colored("Select an option: ", "yellow")).strip()

        if choice == "1":
            password_analyzer.password_analyzer_cli()
        elif choice == "2":
            password_suggestions.password_suggestions_cli() 
        elif choice == "3":
            hash_generator.hash_generator_cli()
        elif choice == "4":
            hash_cracker.hash_cracker_cli()
       elif choice == "5":
            website_scanner.website_scanner_cli()
        elif choice == "6":
            documentation.documentation_cli()
        elif choice == "0":
            print(colored("\nExiting VulnCrypt. Stay ethical!", "red", attrs=["bold"]))
            sys.exit(0)
        else:
            print(colored("Invalid choice, try again!", "red"))
            time.sleep(0.7)

if __name__ == "__main__":
    main()
