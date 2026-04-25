import os 
import shutil

def copy_files_recursive(source_dir, dest_dir):
    # Make sure destination exists
    # (hint: os.mkdir, but only if it doesn't already exist)
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)


    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            # it's a directory — recurse!
            copy_files_recursive(source_path, dest_path)