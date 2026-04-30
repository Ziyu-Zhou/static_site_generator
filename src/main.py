print("hello world")
from textnode import TextNode, TextType
from copystatic import copy_files_recursive
import os
import shutil
import sys
from generator import generate_page, generate_pages_recursive
def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    source_path = "./static"
    dest = "./docs"
    if os.path.exists(dest):
        shutil.rmtree(dest)

    copy_files_recursive(source_path, dest)

    from_path = "content"
    template_path = "template.html"
    dest_path = "docs/"

    
    generate_pages_recursive(from_path, template_path, dest_path, basepath)

    




main()