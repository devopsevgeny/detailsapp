import zipfile
import os
import shutil

def find_file_recursively(root, target):
    for dirpath, dirnames, filenames in os.walk(root):
        if target in filenames:
            return os.path.join(dirpath, target)
    return None

def find_dir_recursively(root, target):
    for dirpath, dirnames, filenames in os.walk(root):
        if target in dirnames:
            return os.path.join(dirpath, target)
    return None

def unzip_and_move(archive_path):
    if not archive_path or not os.path.exists(archive_path):
        print("❌ Archive not found.")
        return

    base_dir = os.path.dirname(archive_path)
    extract_dir = os.path.join(base_dir, "temp_extract")

    # Clean up temp folder if it already exists
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    os.makedirs(extract_dir)

    print(f"📂 Extracting {archive_path}...")
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"✅ Extracted to {extract_dir}")

    try:
        # Find and move index.html
        index_path = find_file_recursively(extract_dir, "index.html")
        if index_path:
            target_template = os.path.join("src", "details", "templates", "index.html")
            os.makedirs(os.path.dirname(target_template), exist_ok=True)

            if os.path.exists(target_template):
                print(f"⚠️ index.html already exists — skipping.")
            else:
                shutil.move(index_path, target_template)
                print(f"📄 Moved index.html to {target_template}")
        else:
            print("⚠️ index.html not found.")

        # Find and move asset folders
        for folder in ["css", "js", "assets"]:
            folder_path = find_dir_recursively(extract_dir, folder)
            if folder_path:
                target_folder = os.path.join("src", "details", "static", folder)
                os.makedirs(os.path.dirname(target_folder), exist_ok=True)

                if os.path.exists(target_folder):
                    print(f"⚠️ {folder}/ already exists — skipping.")
                else:
                    shutil.move(folder_path, target_folder)
                    print(f"📁 Moved {folder}/ to {target_folder}")
            else:
                print(f"⚠️ {folder}/ folder not found.")

        print("✅ All available files moved successfully.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    # Clean up
    shutil.rmtree(extract_dir)
    print("🧹 Temporary folder cleaned up.")
