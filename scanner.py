import os
from dotenv import load_dotenv
# Imports the tools we need to read environment variables and use the Google API
import google.generativeai as genai
from colorama import init, Fore, Style
import sys


# Initialize colorama
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()
# Loads variables from your .env file into the environment

# Configure with your API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
# Retrieves your API key from the environment (keeps it out of your code)

genai.configure(api_key=api_key)
# Sets up authentication with your API key

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash")
# Creates a model object for Gemini 2.5 Flash, which is fast and efficient for text tasks
# Vulnerable code example 1: SQL Injection
vulnerable_code_1 = '''
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()
'''

# Vulnerable code example 2: Hardcoded credentials
vulnerable_code_2 = '''
DATABASE_PASSWORD = "supersecret123"
API_KEY = "sk-1234567890abcdef"

def connect_db():
    return psycopg2.connect(
        host="localhost",
        password=DATABASE_PASSWORD
    )
'''

# Vulnerable code example 3: Weak cryptography
vulnerable_code_3 = '''
import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
'''
security_prompt = """
Analyze this code for security vulnerabilities. Be concise.

For each issue use this exact format:

---
SEVERITY: [CRITICAL/HIGH/MEDIUM/LOW]

**TYPE:** [Vulnerability Name] \n
**DESCRIPTION:** [One sentence explaining the issue] \n
**IMPACT:** [One sentence on potential damage] \n

**FIX:** [Code snippet only] \n
---

Code:
{code}
"""

def add_colors_to_output(text):
    """Add colors to severity levels in the output."""
    text = text.replace("SEVERITY: CRITICAL", f"SEVERITY: {Fore.RED}{Style.BRIGHT}CRITICAL{Style.RESET_ALL}")
    text = text.replace("SEVERITY: HIGH", f"SEVERITY: {Fore.YELLOW}{Style.BRIGHT}HIGH{Style.RESET_ALL}")
    text = text.replace("SEVERITY: MEDIUM", f"SEVERITY: {Fore.BLUE}MEDIUM{Style.RESET_ALL}")
    text = text.replace("SEVERITY: LOW", f"SEVERITY: {Fore.GREEN}LOW{Style.RESET_ALL}")
    return text

def scan_file(filepath):
    """Read a file and analyze it for vulnerabilities."""
    try:
        with open(filepath, 'r') as f:
            code = f.read()

        print(f"\n{'=' * 60}")
        print(f"Scanning: {filepath}")
        print(f"{'=' * 60}\n")

        # Use the existing security prompt
        response = model.generate_content(security_prompt.format(code=code))
        output = add_colors_to_output(response.text)
        print(output)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File '{filepath}' not found.{Style.RESET_ALL}")

def run_analysis_for_web(code_content):
    """Function that adds colors specifically for the Streamlit website."""
    full_prompt = security_prompt.format(code=code_content)
    response = model.generate_content(full_prompt)
    text = response.text
    
    # These lines translate the labels into colored Markdown for Streamlit
    text = text.replace("SEVERITY: CRITICAL", "### :red[SEVERITY: CRITICAL]")
    text = text.replace("SEVERITY: HIGH", "### :orange[SEVERITY: HIGH]")
    text = text.replace("SEVERITY: MEDIUM", "### :blue[SEVERITY: MEDIUM]")
    text = text.replace("SEVERITY: LOW", "### :green[SEVERITY: LOW]")
    
    return text
# ============================================================
# YOUR CODE GOES BELOW HERE
# ============================================================

# Check if a filename was provided
if len(sys.argv) > 1:
    filepath = sys.argv[1]
    print(f"Scanning file: {filepath}\n")
    scan_file(filepath)
else:
    print("Usage: python scanner.py <filepath>")
    print("Example: python scanner.py vulnerable.py")



# ============================================================
# YOUR CODE GOES ABOVE HERE
# ============================================================
