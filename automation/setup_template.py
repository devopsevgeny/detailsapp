import os
from automation.download_template import download_template
from automation.unzip_and_move import unzip_and_move
from automation.update_index_html import update_index_links

def main():
    print("📦 Step 1: Download template")
    archive = download_template()
    if not archive:
        print("❌ Aborting: Failed to download template.")
        return

    print("\n🗂️ Step 2: Unzip and move files")
    unzip_and_move(archive)

    index_path = os.path.join("src", "details", "templates", "index.html")
    if os.path.exists(index_path):
        print("\n🛠️ Step 3: Update index.html paths")
        update_index_links()
    else:
        print(f"\n⚠️ Skipping Step 3: index.html not found at {os.path.abspath(index_path)}")

    print("\n🎉 Done!")

if __name__ == "__main__":
    main()
