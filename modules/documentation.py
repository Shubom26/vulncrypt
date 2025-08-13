#!/home/kali/vulncrypt/venv/bin/python3

import os
import pyfiglet
from termcolor import colored
import time

def print_separator():
    print(colored("=" * 60, "cyan"))

def show_banner():
    os.system("clear")
    banner = pyfiglet.figlet_format("VulnCrypt Docs")
    print(colored(banner, "cyan", attrs=["bold"]))

def documentation_cli():
    show_banner()
    print_separator()
    print(colored("VulnCrypt: Comprehensive Security Toolkit\n", "yellow", attrs=["bold"]))

    print(colored("Overview", "magenta", attrs=["underline", "bold"]))
    print("VulnCrypt is a professional, command-line-based cybersecurity toolkit designed for ethical security practitioners, penetration testers, and learners.")
    print("Developed by Y Kabir Singha and Shubom Deb as part of a cybersecurity internship at the Silchar Extension Centre of NIELIT, Guwahati,")
    print("this toolkit combines multiple essential security utilities under one roof.\n")
    print("The primary goal of VulnCrypt is to provide a modular, easy-to-use platform for password analysis, hash operations, and basic website vulnerability scanning, with a strong emphasis on ethical use.\n")

    print(colored("Modules Included", "magenta", attrs=["underline", "bold"]))
    print(colored("1. Password Strength Analyzer", "cyan", attrs=["bold"]))
    print("   Purpose: Analyze and rate the strength of passwords based on complexity, length, and common weaknesses.\n")
    print("   Features:")
    print("   - Checks for lowercase, uppercase, digits, and symbols.")
    print("   - Penalizes repeated characters and common weak patterns.")
    print("   - Estimates the time required to crack the password using brute force.")
    print("   - Provides a user-friendly CLI with color-coded strength feedback.\n")
    print("   Usage: Enter any password to receive a strength score, qualitative rating (Very Weak to Very Strong), and estimated crack time.\n")

    print(colored("2. Password Suggestions Generator", "cyan", attrs=["bold"]))
    print("   Purpose: Generate strong, random passwords tailored to user-specified criteria.\n")
    print("   Features:")
    print("   - Choose to include uppercase, lowercase, digits, and/or symbols.")
    print("   - Minimum length enforcement with dynamic adjustment.")
    print("   - Ensures generated password contains at least one character from each selected set.")
    print("   - Simple CLI prompts with loading animation and retry option.\n")
    print("   Usage: Select character sets and desired length; generate as many passwords as needed.\n")

    print(colored("3. Hash Password Cracker", "cyan", attrs=["bold"]))
    print("   Purpose: Attempt to find the plaintext corresponding to a given hash by brute forcing with a wordlist.\n")
    print("   Features:")
    print("   - Supports MD5, SHA-1, SHA-256, and SHA-512 hashes.")
    print("   - Uses the popular rockyou.txt password list for cracking.")
    print("   - Provides progress feedback every 100,000 attempts.")
    print("   - Displays elapsed time and cracked password if found.\n")
    print("   Usage: Input a hash and specify the hash type; the tool attempts to find a matching password.\n")

    print(colored("4. Hash Generator", "cyan", attrs=["bold"]))
    print("   Purpose: Generate hash digests of any text input for commonly used hashing algorithms.\n")
    print("   Features:")
    print("   - Supports MD5, SHA-1, SHA-256, and SHA-512.")
    print("   - Clear CLI interface with input validation.")
    print("   - Loading animation for better user experience.\n")
    print("   Usage: Input text and select hash type; receive the hash digest output instantly.\n")

    print(colored("5. Website Vulnerability Scanner (Basic)", "cyan", attrs=["bold"]))
    print("   Purpose: Perform preliminary security assessment of websites by scanning open ports and checking HTTP security headers.\n")
    print("   Features:")
    print("   - Resolves domain to IP.")
    print("   - Scans common ports for open services.")
    print("   - Retrieves HTTP headers and analyzes presence of critical security headers (e.g., HSTS, CSP, X-Frame-Options).")
    print("   - Checks SSL/TLS certificate details including issuer and validity.")
    print("   - Fetches and displays robots.txt contents if available.")
    print("   - Includes an ethical use warning and requires user confirmation before scanning.\n")
    print("   Usage: Input a website domain or URL to receive an easy-to-read security report.\n")

    print(colored("Ethical Use & Legal Testing Guidelines", "magenta", attrs=["underline", "bold"]))
    print("VulnCrypt is intended strictly for ethical use on systems and websites you own or have explicit, written permission to test.")
    print("Unauthorized scanning or password cracking attempts against systems you do not own or lack permission for are illegal and punishable by law.\n")

    print(colored("Websites You Can Test Legally", "magenta", attrs=["underline", "bold"]))
    print("You can safely practice scanning and vulnerability assessment on the following:")
    print("- Your own websites and servers — any domain or IP address you control.")
    print("- Public bug bounty programs — platforms like HackerOne, Bugcrowd, Synack, where the scope and rules are clearly defined.")
    print("- Intentionally vulnerable websites for practice:")
    print("  * OWASP Juice Shop")
    print("  * DVWA (Damn Vulnerable Web Application)")
    print("  * Hack The Box (lab environments)")
    print("  * VulnHub (download vulnerable VMs)")
    print("  * bWAPP")
    print("  * CTF (Capture The Flag) platforms with legally provided vulnerable machines or challenges.\n")
    print("Always read and adhere to the terms of service, scope, and rules of engagement for any third-party platforms or systems before testing.\n")

    print(colored("Disclaimer", "magenta", attrs=["underline", "bold"]))
    print("This toolkit is provided for educational and authorized security testing purposes only.")
    print("The authors do not take responsibility for misuse or illegal activities conducted with VulnCrypt.")
    print("Always operate within the bounds of applicable laws and ethical standards.\n")

    print_separator()
    input(colored("Press Enter to return to main menu...", "yellow"))

if __name__ == "__main__":
    documentation_cli()
