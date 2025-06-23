import os
import glob

def rename_files(folder_path, prefix):
    os.chdir(folder_path)
    files = glob.glob("*.*")  # Matches all files

    for i, filename in enumerate(files):
        name, ext = os.path.splitext(filename)
        new_name = f"{prefix}_{i+1}{ext}"
        os.rename(filename, new_name)
        print(f"Renamed: {filename} → {new_name}")
