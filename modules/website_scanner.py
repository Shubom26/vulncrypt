#!/home/kali/vulncrypt/venv/bin/python3

import socket
import ssl
import requests
import urllib.parse
import time
import sys
import os
import pyfiglet
from termcolor import colored

def print_separator():
    print(colored("=" * 60, "cyan"))

def show_banner():
    os.system("clear")
    banner = pyfiglet.figlet_format("VulnScanner")
    print(colored(banner, "cyan", attrs=["bold"]))

def ethical_warning():
    print_separator()
    print(colored("⚠️  Ethical Use Warning", "red", attrs=["bold"]))
    print(colored("Only scan websites you own or have explicit permission to test.", "yellow"))
    print(colored("Unauthorized scanning is illegal and unethical.", "yellow"))
    print_separator()
    choice = input(colored("Do you want to continue? (y/n): ", "yellow")).strip().lower()
    if choice != 'y':
        print(colored("\nScan cancelled. Returning to main menu...\n", "magenta"))
        time.sleep(1)
        return False
    return True

def resolve_domain(url):
    try:
        domain = urllib.parse.urlparse(url).netloc or url
        if ':' in domain:
            domain = domain.split(':')[0]
        ip = socket.gethostbyname(domain)
        return domain, ip
    except Exception as e:
        print(colored(f"Error resolving domain: {e}", "red"))
        return None, None

def scan_ports(ip, ports=None):
    if ports is None:
        # Common ports to scan
        ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]

    print(colored(f"\nStarting port scan on {ip} ...\n", "yellow"))
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                print(colored(f"Port {port} is OPEN", "green"))
            sock.close()
        except Exception:
            sock.close()
    if not open_ports:
        print(colored("No common open ports found.", "red"))
    return open_ports

def fetch_http_headers(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        response = requests.get(url, timeout=5)
        return response.headers, response.status_code
    except Exception as e:
        print(colored(f"Failed to fetch HTTP headers: {e}", "red"))
        return None, None

def analyze_security_headers(headers):
    print(colored("\nAnalyzing HTTP Security Headers...", "yellow"))
    important_headers = {
        "Strict-Transport-Security": "HTTP Strict Transport Security (HSTS)",
        "Content-Security-Policy": "Content Security Policy (CSP)",
        "X-Frame-Options": "Clickjacking protection",
        "X-Content-Type-Options": "MIME-sniffing protection",
        "Referrer-Policy": "Referrer information control",
        "Permissions-Policy": "Feature policy control"
    }

    for header, description in important_headers.items():
        if header in headers:
            print(colored(f"[+] {description}: Present", "green"))
        else:
            print(colored(f"[-] {description}: MISSING", "red"))

def check_ssl_certificate(domain):
    print(colored("\nChecking SSL/TLS Certificate Information...", "yellow"))
    context = ssl.create_default_context()
    try:
        with socket.create_connection((domain, 443), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                issuer = dict(x[0] for x in cert['issuer'])
                issued_to = dict(x[0] for x in cert['subject'])
                valid_from = cert['notBefore']
                valid_to = cert['notAfter']
                print(colored(f"Certificate Issuer: {issuer.get('organizationName', 'Unknown')}", "green"))
                print(colored(f"Certificate Subject: {issued_to.get('commonName', 'Unknown')}", "green"))
                print(colored(f"Valid From: {valid_from}", "green"))
                print(colored(f"Valid To: {valid_to}", "green"))
    except Exception as e:
        print(colored(f"Failed to retrieve SSL certificate: {e}", "red"))

def check_robots_txt(domain):
    url = f"http://{domain}/robots.txt"
    print(colored(f"\nChecking robots.txt at {url} ...", "yellow"))
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(colored("robots.txt found. Contents:", "green"))
            print(colored(response.text, "blue"))
        else:
            print(colored("robots.txt not found or inaccessible.", "red"))
    except Exception as e:
        print(colored(f"Error fetching robots.txt: {e}", "red"))

def website_scanner_cli():
    show_banner()
    print(colored("Welcome to the Website Vulnerability Scanner\n", "yellow", attrs=["bold"]))
    url = input(colored("Enter target URL or domain (e.g. example.com): ", "green")).strip()
    if not url:
        print(colored("No URL provided. Returning to main menu...\n", "magenta"))
        time.sleep(1)
        return

    domain, ip = resolve_domain(url)
    if not domain or not ip:
        print(colored("Failed to resolve domain. Returning to main menu...\n", "red"))
        time.sleep(2)
        return

    print_separator()
    print(colored(f"Resolved domain {domain} to IP: {ip}", "cyan"))

    if not ethical_warning():
        return

    open_ports = scan_ports(ip)
    print_separator()

    headers, status_code = fetch_http_headers(domain)
    if headers:
        print(colored(f"\nHTTP Status Code: {status_code}", "cyan"))
        analyze_security_headers(headers)
    else:
        print(colored("Could not retrieve HTTP headers.", "red"))

    check_ssl_certificate(domain)
    check_robots_txt(domain)

    print_separator()
    print(colored("Scan Complete! Review the results above.\n", "green", attrs=["bold"]))
    input(colored("Press Enter to return to main menu...", "yellow"))

if __name__ == "__main__":
    website_scanner_cli()
