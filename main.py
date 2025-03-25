import requests
from urllib.parse import urljoin
import sys

def process_wordlist(filePath):
    try:
        with open(filePath, 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print(f"Error: File '{filePath}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

# Function to get the no. of words in the wordlist
def file_word_count(filePath):
    file = open(filePath,  'r')
    contents = file.read()
    file.close()

    word_count = contents.split()
    num_words = len(word_count)

    return num_words


# Function to check for a directory
def check_directory(url, directory):
    full_url = urljoin(url, directory)
    try:
        # Add a timeout to prevent hanging on slow responses
        response = requests.get(full_url, timeout=5)
        
        # Log all responses with directory name, URL and status code
        if response.status_code == 200:
            print(f'[+] Directory: "{directory}" - {full_url} [+] Status code: {response.status_code}')
        elif response.status_code == 301 or response.status_code == 302:
            print(f'[+] Directory (redirect): "{directory}" - {full_url} [+] Status code: {response.status_code}')
        elif response.status_code == 400:
            # Log other status codes with directory name
            print(f'[-] Directory: "{directory}" - {full_url} [-] Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'[-] Error checking "{directory}" - {full_url}: {e}')

def main():
    print('''*
    .______      ___   .___________. __    __  .______    __    __       _______.___________. _______ .______      
|   _  \    /   \  |           ||  |  |  | |   _  \  |  |  |  |     /       |           ||   ____||   _  \     
|  |_)  |  /  ^  \ `---|  |----`|  |__|  | |  |_)  | |  |  |  |    |   (----`---|  |----`|  |__   |  |_)  |    
|   ___/  /  /_\  \    |  |     |   __   | |   _  <  |  |  |  |     \   \       |  |     |   __|  |      /     
|  |     /  _____  \   |  |     |  |  |  | |  |_)  | |  `--'  | .----)   |      |  |     |  |____ |  |\  \----.
| _|    /__/     \__\  |__|     |__|  |__| |______/   \______/  |_______/       |__|     |_______|| _| `._____|
                                                                                                                
          *''')
    base_url = input("Enter the base URL: ")
    if len(sys.argv) < 2:
        print("Usage: python main.py <wordlist_file>")
        sys.exit(1)

    # Get the filename from command line argument
    filename = sys.argv[1]

    # Process the wordlist
    common_dirs = process_wordlist(filename)

    # Get Word Count:
    word_count = file_word_count(filename)

    print(f"\nScanning {base_url} with {word_count} directories...\n")

    count = 0

    # Printing initial progress
    print(f"Progress: {count} / {word_count}", end='', flush=True)

    for directory in common_dirs:
        check_directory(base_url, directory)
        count = count + 1
        print(f"\rProgess: {count} / {word_count}", end='', flush=True)


    print("\nScan complete!")


if __name__ == "__main__":
    main()

