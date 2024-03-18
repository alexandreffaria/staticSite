import os
import shutil
from copyStatic import copyRecursively

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public folder.")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public dir...")
    copyRecursively(dir_path_static, dir_path_public)

if __name__ == "__main__":
    main()

