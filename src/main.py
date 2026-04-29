print("hello world")
from textnode import TextNode, TextType
from copystatic import copy_files_recursive
import os
import shutil
from generator import generate_page, generate_pages_recursive
def main():

    source_path = "./static"
    dest = "./public"
    if os.path.exists(dest):
        shutil.rmtree(dest)

    copy_files_recursive(source_path, dest)

    from_path = "content"
    template_path = "template.html"
    dest_path = "public/"

    
    generate_pages_recursive(from_path, template_path, dest_path)

    




main()