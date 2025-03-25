# PathBuster
# PathBuster: A Simple Directory Bruteforcer

## Overview
**PathBuster** is a Python-based directory brute-forcing tool designed to scan a target URL for common directories using a wordlist inspired by **Gobuster**. It logs valid directories, handles redirects, and provides real-time progress tracking.

## Features
- 🚀 **Fast & Simple**: Scans directories from a wordlist efficiently.
- 🔄 **Handles Redirects**: Detects 301/302 and reports them properly.
- 📊 **Progress Tracking**: Displays scan progress dynamically.
- ⏳ **Timeout Handling**: Prevents hanging on slow responses.
- 🛠️ **Error Logging**: Catches and logs request errors.

## Installation
This tool requires Python 3 and the `requests` library. Install dependencies with:

```bash
pip install requests
```

## Usage
Run the script with a target URL and a wordlist file:

```bash
python main.py <wordlist_file>
```

### Example:
```bash
python main.py common.txt
```

Then, enter the base URL when prompted:
```
Enter the base URL: http://example.com
```

## Output
- **200 OK**: Valid directory found.
- **301/302 Redirect**: Directory redirects.
- **400 Bad Request**: Invalid directory request.
- **Errors**: Logged with the failed directory.

## To-Do (Future Enhancements)
- ✅ Add multi-threading for faster scans.
- ✅ Save valid directories to a log file.
- ✅ Support custom headers for stealth scanning.

## Contributing
Feel free to fork, modify, and improve this tool. PRs are welcome!

## Disclaimer
This tool is for educational and ethical purposes only. Do **not** use it on systems without permission.

---
🚀 **Happy Hacking!** 🛠️


