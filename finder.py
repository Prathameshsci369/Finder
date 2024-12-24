import re
import requests
import time
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
import google.generativeai as genai
from api_validations import validate_key  # Ensure this module is correctly implemented

# Embedded Gemini API key and Generative AI configuration
GEMINI_API_KEY = "ENTER_YOUR_OWN_GEMINI_API_KEY"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


import os
import time
import sys

# Sound effect for "hacker vibe"
def play_beep():
    try:
        # For Windows, use winsound
        if os.name == "nt":
            import winsound
            winsound.Beep(1000, 300)  # Frequency, Duration (ms)
        # For Linux/Mac, use terminal bell
        else:
            print("\a", end='', flush=True)
    except Exception as e:
        print(f"Sound effect error: {e}")

# Function to display the tool name with fancy effects
def display_tool_name():
    # Clear the screen for a clean look
    os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII Art for "FINDER" in green
    tool_name_art = r"""
       ███████╗██╗███╗   ██╗██████╗  
       ██╔════╝██║████╗  ██║██╔══██╗
       ██╔══╝  ██║██║╚██╗██║██║  ██║ 
       ██║     ██║██║ ╚████║██████╔╝   
       ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝    
    """
    print("\033[92m" + tool_name_art + "\033[0m")  # Print in green
    print("\033[93mPentester's Favorite  Sensitive Data Scanner\033[0m")  # Yellow subtitle
    print("\033[94m---------------------------------------------------\033[0m")  # Blue divider
    print("Starting the scan...\n")

    # Simulate a "hacker-style" loading bar
    print("\033[95m[+] Initializing...\033[0m\n")  # Purple for loading message
    for i in range(101):
        sys.stdout.write(f"\r\033[96m[{'=' * (i // 2)}{' ' * (50 - i // 2)}] {i}%\033[0m")
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")
        
# Define the regex patterns
_regex = {
    'google_api': r'AIza[0-9A-Za-z-_]{35}',
    'firebase': r'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}',
    'google_captcha': r'6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
    'google_oauth': r'ya29\.[0-9A-Za-z\-_]+',
    'amazon_aws_access_key_id': r'A[SK]IA[0-9A-Z]{16}',
    'amazon_mws_auth_token': (
        r'amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-'
        r'[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
    ),
    'facebook_access_token': r'EAACEdEose0cBA[0-9A-Za-z]+',
    'authorization_basic': r'basic [a-zA-Z0-9=:_\+\/-]{5,100}',
    'authorization_bearer': r'bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}',
    'authorization_api': r'api[key|_key|\s+]+[a-zA-Z0-9_\-]{5,100}',
    'mailgun_api_key': r'key-[0-9a-zA-Z]{32}',
    'twilio_api_key': r'SK[0-9a-fA-F]{32}',
    'twilio_account_sid': r'AC[a-zA-Z0-9]{60}',
    'twilio_app_sid': r'AP[a-zA-Z0-9]{60}',
    'paypal_braintree_access_token': (
        r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}'
    ),
    'square_oauth_secret': (
        r'sq0csp-[0-9a-zA-Z]{32}|sq0[a-z]{3}-[0-9a-zA-Z]{22,43}'
    ),
    'square_access_token': r'sqOatp-[0-9a-zA-Z]{22}|EAAA[a-zA-Z0-9]{60}',
    'stripe_standard_api': r'sk_live_[0-9a-zA-Z]{24}',
    'stripe_restricted_api': r'rk_live_[0-9a-zA-Z]{24}',
    'github_access_token': r'[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
    'rsa_private_key': (
        r'-----BEGIN RSA PRIVATE KEY-----[\s\S]+?-----END RSA PRIVATE KEY-----'
    ),
    'ssh_dsa_private_key': r'-----BEGIN DSA PRIVATE KEY-----',
    'ssh_dc_private_key': r'-----BEGIN EC PRIVATE KEY-----',
    'pgp_private_block': r'-----BEGIN PGP PRIVATE KEY BLOCK-----',
    'json_web_token': r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
    'slack_token': r'"api_token":"(xox[a-zA-Z]-[a-zA-Z0-9-]+)"',
    'SSH_privKey': (
        r"([-]+BEGIN [^\s]+ PRIVATE KEY[-]+[\s]*[^-]*[-]+END [^\s]+ PRIVATE KEY[-]+)"
    ),
    'Heroku API KEY': (
        r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-'
        r'[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'
    ),
    'possible_Creds': r"(?i)(password\s*[`=:\"]+\s*[^\s]+)",
    'password': r'password\s*[`=:\"]+\s*[^\s]+'
}


# Function to extract JavaScript files using Playwright
def get_js_files(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            page.wait_for_load_state("load")

            js_files = []
            scripts = page.query_selector_all("script[src]")
            for script in scripts:
                script_url = script.get_attribute("src")
                if script_url:
                    full_url = urljoin(url, script_url)
                    js_files.append(full_url)

            browser.close()
        return js_files
    except Exception as e:
        print(f"\n Error extracting JavaScript files: {e}\n")
        return []

# Function to find sensitive info in JS content
def find_sensitive_info(js_content, js_file, results):
    for key, pattern in _regex.items():
        matches = re.findall(pattern, js_content)
        if matches:
            if key not in results:
                results[key] = {"valid_matches": [], "unvalidated_matches": []}

            for match in matches:
                if validate_key(key, match):  # Assume validate_key is implemented
                    results[key]["valid_matches"].append((match, js_file))
                    print(f"\nValid match found: {match} (Source: {js_file}) \n")
                else:
                    results[key]["unvalidated_matches"].append((match, js_file))
                    print(f"\nUnvalidated match found: {match} (Source: {js_file})\n")

# Function to save raw output with valid keys on top
def save_raw_output(results, filename="raw_output.txt"):
    try:
        with open(filename, "w") as file:
            file.write("--- VALID MATCHES ---\n")
            for key, value in results.items():
                for match, js_file in value.get("valid_matches", []):
                    file.write(f"{match} (Source: {js_file})\n")

            file.write("\n--- UNVALIDATED MATCHES ---\n")
            for key, value in results.items():
                for match, js_file in value.get("unvalidated_matches", []):
                    file.write(f"{match} (Source: {js_file})\n")
        print(f"Raw output saved as {filename}")
    except Exception as e:
        print(f"Error saving raw output: {e}")

# Function to analyze raw output with Gemini API (with retry mechanism)
def analyze_with_gemini(report_file="raw_output.txt", max_retries=6, retry_delay=5):
    gemini_api_url = "https://gemini.api/analyze"  # Replace with actual Gemini API URL
    for attempt in range(max_retries):
        try:
            with open(report_file, "rb") as file:
                headers = {
                    "Authorization": f"Bearer {GEMINI_API_KEY}"  # Embedded Gemini API key
                }
                files = {
                    "file": file
                }

                response = requests.post(gemini_api_url, headers=headers, files=files)

                if response.status_code == 200:
                    analysis_result = response.json()  # Assuming the response is in JSON format
                    print("Gemini analysis completed successfully.")
                    return analysis_result
                else:
                    print(f"Error analyzing report with Gemini: {response.text}")
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")

        print(f"Retrying in {retry_delay} seconds...")
        time.sleep(retry_delay)

    print("Failed to analyze report with Gemini after multiple attempts.")
    return None

# Function to get AI-generated explanation for sensitive information
def get_ai_explanation(key):
    try:
        prompt = f"Explain why exposure of {key} is dangerous in cybersecurity."
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating explanation for {key}: {e}")
        return "No explanation available."

# Function to save structured report based on Gemini analysis
def save_structured_report(analysis_result, filename="structured_report.txt"):
    try:
        with open(filename, "w") as file:
            file.write("PENTESTING REPORT\n")
            file.write("=================\n")
            file.write("Gemini Analysis Results:\n\n")
            for item in analysis_result.get("results", []):
                key = item.get("key")
                status = item.get("status")
                details = item.get("details", "No additional details")
                source_files = item.get("source_files", [])

                file.write(f"--- {key} ---\n")
                file.write(f"Status: {status.capitalize()}\n")
                file.write(f"Details: {details}\n")
                file.write("Source Files:\n")
                for source_file in source_files:
                    file.write(f"  - {source_file}\n")
                
                # Add AI-generated explanation
                explanation = get_ai_explanation(key)
                file.write(f"AI Explanation: {explanation}\n\n")
            file.write("END OF REPORT\n")
        print(f"Structured report saved as {filename}")
    except Exception as e:
        print(f"Error saving structured report: {e}")

# Main function
def main(url):
    play_beep()
    display_tool_name()
    try:
        js_files = get_js_files(url)
        if not js_files:
            print("No JavaScript files found.")
            return

        results = {}
        for js_file in js_files:
            try:
                response = requests.get(js_file)
                response.raise_for_status()
                find_sensitive_info(response.text, js_file, results)
            except requests.RequestException as e:
                print(f"Error fetching {js_file}: {e}")

        # Save raw output with all findings
        raw_output_file = "raw_output.txt"
        save_raw_output(results, raw_output_file)

        # Analyze raw output with Gemini API (with retry logic)
        analysis_result = analyze_with_gemini(report_file=raw_output_file)

        # Save structured report based on Gemini analysis
        if analysis_result:
            save_structured_report(analysis_result)
        else:
            print("No valid analysis result from Gemini API.")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the website to scan: ")
    main(url)
