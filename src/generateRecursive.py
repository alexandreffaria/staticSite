import os
from gencontent import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirList = os.listdir(dir_path_content)
    for dirItem in dirList:
        if dirItem.endswith(".md"):
            generate_page(os.path.join(dir_path_content, dirItem), template_path, dest_dir_path)
        if os.path.isdir(os.path.join(dir_path_content, dirItem)):
            generate_pages_recursive(os.path.join(dir_path_content, dirItem), template_path, dest_dir_path)
