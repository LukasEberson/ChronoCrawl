import pandas as pd
import re

def extract_urls(text):
    return re.findall(r'https?://[^\s]+', text)

def load_urls_from_file(path):
    if path.endswith('.csv'):
        df = pd.read_csv(path)
        urls = df[df.columns[0]].dropna().tolist()
    elif path.endswith('.xlsx'):
        df = pd.read_excel(path)
        urls = df[df.columns[0]].dropna().tolist()
    elif path.endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        urls = extract_urls(content)
    else:
        raise ValueError("Unsupported file type.")
    return urls
