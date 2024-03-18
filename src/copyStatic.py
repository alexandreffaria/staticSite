import os, shutil

def copyRecursively(cpPath, targetPath):
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)
    
    for filename in os.listdir(cpPath):
        from_path = os.path.join(cpPath, filename)
        to_path = os.path.join(targetPath, filename)
        print(f" * {from_path} -> {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copyRecursively(from_path, to_path)
