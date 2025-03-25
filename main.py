import requests
from urllib.parse import urljoin
import sys

# list of common directories for now
common_dirs = []

def process_wordlist(filePath):
    try:
        with open(filePath, 'r') as file:
            words = file.read().splitlines()
            common_dirs.append(words)
    except FileNotFoundError:
        print(f"Error: File '{filePath}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

# Function to check for a directory
def check_directory(url, directory):
    full_url = urljoin(url, directory) # Combine base URL with the directory
    try:
        # Send GET request to the directory URL
        response = requests.get(full_url)
        # Check for a valid response code (e.g. 200 or 301)
        if response.status_code == 200:
            print(f'[+] Found directory: {full_url} [+] Status code: {response.status_code}')
        elif response.status_code == 301 or response.status_code == 302:
            print(f"[+] Found directory (redirect): {full_url} [+] Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
            print(f"[-] Error: {e}")

def main():
    base_url = input("Enter the base URL: ") 
    if len(sys.argv) < 2:
        print("UsageL python main.py <wordlist_file>")
        sys.exit(1)

    # Get the filename from command line argument
    filename = sys.argv[1]

    # Process the wordlist
    words = process_wordlist(filename)

    for directory in common_dirs:
            check_directory(base_url, directory)


if __name__ == "__main__":
    main()
