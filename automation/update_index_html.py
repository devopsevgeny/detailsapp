import os
import shutil
import re

def update_index_links(resource_folders=None):
    """
    Update all static resource links in index.html to use Flask's url_for function.
    
    Args:
        resource_folders (list, optional): List of resource folder prefixes to process.
                                          Defaults to ['css/', 'js/', 'assets/', 'images/', 'img/', 'fonts/'].
    
    Returns:
        bool: True if successful, False otherwise.
    """
    # Default resource folders if none provided
    if resource_folders is None:
        resource_folders = ['css/', 'js/', 'assets/', 'images/', 'img/', 'fonts/']
    
    try:
        # Setup paths
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        template_path = os.path.join(project_root, "src", "details", "templates", "index.html")
        backup_path = os.path.join(project_root, "src", "details", "templates", "index_backup.html")
        
        # Check if file exists
        if not os.path.exists(template_path):
            print(f"❌ index.html not found at: {template_path}")
            return False
        
        # Create backup
        shutil.copy2(template_path, backup_path)
        print(f"📋 Created backup at: {backup_path}")
        
        # Read template content
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Track number of replacements
        total_replacements = 0
        
        # Process for double quoted attributes
        for folder in resource_folders:
            for prefix in ['', '/']:
                # Double quotes href
                pattern = f'href="{prefix}{folder}([^"]+)"'
                replacement = f'href="{{{{ url_for(\'static\', filename=\'{folder}\\1\') }}}}"'
                new_content, count = re.subn(pattern, replacement, content)
                if count > 0:
                    content = new_content
                    total_replacements += count
                
                # Double quotes src
                pattern = f'src="{prefix}{folder}([^"]+)"'
                replacement = f'src="{{{{ url_for(\'static\', filename=\'{folder}\\1\') }}}}"'
                new_content, count = re.subn(pattern, replacement, content)
                if count > 0:
                    content = new_content
                    total_replacements += count
                
                # Single quotes href
                pattern = f"href='{prefix}{folder}([^']+)'"
                replacement = f'href="{{{{ url_for(\'static\', filename=\'{folder}\\1\') }}}}"'
                new_content, count = re.subn(pattern, replacement, content)
                if count > 0:
                    content = new_content
                    total_replacements += count
                
                # Single quotes src
                pattern = f"src='{prefix}{folder}([^']+)'"
                replacement = f'src="{{{{ url_for(\'static\', filename=\'{folder}\\1\') }}}}"'
                new_content, count = re.subn(pattern, replacement, content)
                if count > 0:
                    content = new_content
                    total_replacements += count
        
        # Write updated content
        with open(template_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"✅ index.html updated with {total_replacements} url_for() replacements.")
        return True
        
    except Exception as e:
        print(f"❌ Error updating index.html: {str(e)}")
        # If we created a backup and encountered an error, restore from backup
        if 'backup_path' in locals() and os.path.exists(backup_path):
            try:
                shutil.copy2(backup_path, template_path)
                print("🔄 Restored original file from backup.")
            except Exception as restore_error:
                print(f"⚠️ Failed to restore from backup: {str(restore_error)}")
        return False

if __name__ == "__main__":
    update_index_links()