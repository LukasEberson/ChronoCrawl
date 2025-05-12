import requests
from bs4 import BeautifulSoup

def check_urls(urls):
    results = []
    headers = {"User-Agent": "Mozilla/5.0 (compatible; ChronoCrawl/1.0)"}

    for i, url in enumerate(urls, start=1):
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                text = soup.get_text()
                if "2025" in text:
                    status = "✅ Active (2025 found)"
                else:
                    status = "⚠️ Online but not current"
            else:
                status = f"❌ HTTP {r.status_code}"
        except Exception as e:
            status = f"❌ Error: {str(e).split(':')[0]}"

        print(f"[{i}/{len(urls)}] {url} --> {status}")
        results.append({"URL": url, "Status": status})

    return results
