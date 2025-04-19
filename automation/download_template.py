import os
import requests
from InquirerPy import inquirer

def read_file_list(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def download_file(url):
    filename = url.split("/")[-1]
    print(f"\n⬇️ Downloading: {url}")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Download complete: {filename}")
        return os.path.abspath(filename)
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to download: {e}")
        return None

# ✅ This is what your orchestrator (setup_template.py) imports
def download_template():
    try:
        file_list = read_file_list("bootstrap_templates.txt")
    except FileNotFoundError:
        print("❌ File 'bootstrap_templates.txt' not found.")
        return None

    if not file_list:
        print("⚠️ No templates found.")
        return None

    selected_url = inquirer.select(
        message="📦 Select a template to download:",
        choices=file_list,
        cycle=True,
    ).execute()

    return download_file(selected_url)
