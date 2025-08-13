<h1 align="center">🔐 VulnCrypt</h1>

<p align="center">
  <em>A powerful toolkit for password security, hash operations, and website vulnerability scanning.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Version-1.0-green" alt="Version">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-orange" alt="License">
</p>

---

## 📌 Overview

*VulnCrypt* is a multifunctional security tool designed for:
- *Password Strength Analysis*
- *Strong Password Suggestions*
- *Hash Cracking & Generation*
- *Website Vulnerability Scanning*
- *Built-in Documentation Viewer*

Its goal is to help security researchers, penetration testers, and developers *assess and improve security* with ease.

---

## 🚀 Features

✅ *Password Analyzer* – Check strength, entropy, and security level of passwords.  
✅ *Password Suggestions* – Generate strong, hard-to-crack passwords.  
✅ *Hash Cracker* – Attempt to crack hashes using common wordlists.  
✅ *Hash Generator* – Create hashes using popular algorithms like MD5, SHA256, etc.  
✅ *Website Scanner* – Scan for vulnerabilities, check SSL, and identify security headers.  
✅ *Documentation* – Quickly view built-in guides for each module.

---

## 🛠 How It Works

1. *Password Analyzer*
   - Uses regex rules & entropy calculations to measure password strength.
   - Checks for uppercase, lowercase, numbers, symbols, and length.

2. *Password Suggestions*
   - Creates random secure passwords with a customizable length.
   - Avoids common dictionary words.

3. *Hash Cracker*
   - Compares the given hash against a wordlist.
   - Supports MD5, SHA1, SHA256, and more.

4. *Hash Generator*
   - Converts input text into chosen hash algorithm output.
   - Useful for storing and comparing credentials securely.

5. *Website Scanner*
   - Resolves *domain name → IP address*.
   - Uses socket.gethostbyname() to fetch the IP.
   - Checks server SSL certificate, response headers, and security flags.

---

## 📦 Installation

# Clone the repository
git clone https://github.com/Shubom26/VulnCrypt.git

# Navigate into the project folder
cd VulnCrypt

# Install dependencies
pip install -r requirements.txt

# Run the script
python vulncrypt.py
