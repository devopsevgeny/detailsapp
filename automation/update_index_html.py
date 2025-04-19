import os
import shutil

def update_index_links():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    template_path = os.path.join(project_root, "src", "details", "templates", "index.html")
    backup_path = os.path.join(project_root, "src", "details", "templates", "index_backup.html")

    if not os.path.exists(template_path):
        print(f"❌ index.html not found at: {template_path}")
        return

    shutil.copy(template_path, backup_path)

    with open(template_path, "r") as f:
        content = f.read()

    content = content.replace('href="css/', 'href="/static/css/')
    content = content.replace('src="js/', 'src="/static/js/')
    content = content.replace('src="assets/', 'src="/static/assets/')

    with open(template_path, "w") as f:
        f.write(content)

    print("✅ index.html links updated.")

