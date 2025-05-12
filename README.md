# ChronoCrawl

ChronoCrawl is a terminal-based Python tool that checks if websites from any type of file are still active and up-to-date.
It supports `.txt`, `.csv`, and `.xlsx` input formats and exports results to `.csv` or `.xlsx`.

## Features
- Load URLs from various file types
- Check if websites are reachable (HTTP status)
- Detect if content contains the current year (e.g. 2025)
- Export results in clean tabular format
- Easy-to-use terminal menu

## Installation

1. Clone or download this project.
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Supported input formats

ChronoCrawl accepts three input formats:

- `.txt`: Must contain one URL per line or mixed text with valid `http://` or `https://` links.
- `.csv`: The **first column** should contain URLs (no header required).
- `.xlsx`: Same as `.csv`, with URLs in the **first column**.

Example (`urls.txt`):
```
https://example.com
https://anotherdomain.org/news
```

Example (`urls.csv` or `urls.xlsx`):
```
https://example.com
https://website.net
```

## Step-by-step usage guide

1. Open your terminal or command prompt in the folder containing `main.py`.
2. Run the tool:
```bash
python main.py
```
3. Choose option `1` to load your file (provide full path if needed, e.g. `C:\Users\YourName\Desktop\urls.txt`)
4. Choose option `2` to start checking all URLs (⚠️ Do not close the terminal while scanning)
5. Choose option `3` to export the results (CSV or Excel)
6. Done! Your results will be saved in the project folder.

## Output
- Results are saved as `chrono_results.csv` or `chrono_results.xlsx` in the working directory.

## License
MIT License
