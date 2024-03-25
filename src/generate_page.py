from markdown_blocks import markdown_to_html_node
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Creating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as from_file:
        markdown = from_file.read()
        

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown).split("#")[1]

    new_template = template.replace("{{ Title }}", title)
    new_template = new_template.replace("{{ Content }}", html_content)

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    # Write the updated template to the destination file
    with open(dest_path, "w") as dest_file:  # Use "w" mode to write
        dest_file.write(new_template)


generate_page("content/index.md", "template.html", "public/index.html")
