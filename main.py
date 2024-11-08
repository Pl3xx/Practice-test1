import os

def print_directory_tree(path, indent=""):

    if os.path.isdir(path):
        print(f"{indent}{os.path.basename(path)}/")
        indent += "    "
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print_directory_tree(full_path, indent)
            else:
                print(f"{indent}{entry}")

print_directory_tree("mydir")