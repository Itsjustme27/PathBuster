import requests
from urllib.parse import urljoin

# list of common directories for now
common_dirs = [
        "admin", "login", "uploads", "images"
]

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
    for directory in common_dirs:
            check_directory(base_url, directory)


if __name__ == "__main__":
    main()
