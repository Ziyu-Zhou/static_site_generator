from block_markdown import markdown_to_html_node
import os
from pathlib import Path


def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line.strip()[2:]
    
    raise Exception("no title found")


# def test_extract_title_basic(self):
# md = "# Hello"
# title = extract_title(md)
# print(f"title: {title}")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()


    html = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)
    


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    # contents has all the file or subdirectory in content dir
    
    
    
    contents = os.listdir(dir_path_content)


    # loop throught each item in the content directory
    # check if item is a file or a dir
    # if it's a file, the file should be a index.md run generate page
    # else if it's dir
    # go deeper 
    for item in contents:
        update_path = os.path.join(dir_path_content, item)
        udpated_dest = os.path.join(dest_dir_path, item)
        if os.path.isfile(update_path):
            udpated_dest = Path(udpated_dest).with_suffix(".html")
            generate_page(update_path, template_path, udpated_dest) 
        elif os.path.isdir(update_path):
            generate_pages_recursive(update_path, template_path, udpated_dest)

    

    








