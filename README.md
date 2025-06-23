# 📝 File Renamer

A simple Python script that renames all files in a folder using a custom prefix and automatic numbering. Useful for organizing messy folders, standardizing image/file names, or prepping data.

## 🔧 How It Works

1. You specify a folder path and a prefix.
2. The script renames each file using that prefix and a number (e.g. `project_1.jpg`, `project_2.jpg`, ...).

## 📂 Example

**Before:**

    dog.jpg  
    notes.txt  
    image.png  

**After running the script with prefix `project`:**

    project_1.jpg  
    project_2.txt  
    project_3.png  

## 🚀 Getting Started

1. Clone this repo:

    git clone https://github.com/antmlap/file-renamer.git  
    cd file-renamer

2. Edit the script with your folder path and prefix:

    rename_files("/Users/yourname/Desktop/test-folder", "project")

3. Run the script:

    python3 rename_files.py

## 🧠 Tech Used

- Python 3
- os module
- glob module

## 🛡️ Disclaimer

This script renames **all files** in the target folder. Use a test folder first to avoid renaming important files by accident.
