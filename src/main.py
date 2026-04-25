print("hello world")
from textnode import TextNode, TextType
from copystatic import copy_files_recursive
import os
import shutil

def main():

    source_path = "./static"
    dest = "./public"
    if os.path.exists(dest):
        shutil.rmtree(dest)

    copy_files_recursive(source_path, dest)




main()