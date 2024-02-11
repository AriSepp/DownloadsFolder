import os
import shutil
import glob

def organize_downloads(folder_path):
    # Define file type categories and their corresponding folders
    file_types = {
        "Documents": [".pdf", ".doc", ".docx", ".txt",  ".ppt",  ".pptx", ".xlsx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Code": [".py", ".java"],
        "Music": [".mp3"],
        "Others": []  # Any file types not covered above
        
    }

    # Create destination folders if they don't exist
    for category in file_types:
        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

    # Organize files into designated folders
    for file in glob.glob(os.path.join(folder_path, "*.*")):
        file_extension = os.path.splitext(file)[1].lower()

        # Find the category for the file type
        category = "Others"
        for key, extensions in file_types.items():
            if file_extension in extensions:
                category = key
                break

        # Move the file to the corresponding category folder
        try:
            shutil.move(file, os.path.join(folder_path, category, os.path.relpath(file, folder_path)))
            print_moved_file(file, category)
        except FileNotFoundError:
            print(f"Error: Source file {file} not found.")
        except PermissionError:
            print(f"Error: Can't move {file} due to permission issues.")
        except shutil.Error as e:
            print(f"Error: Failed to move {file}. Reason: {e}")

def print_moved_file(file, category):
    file_name = os.path.basename(file)
    print(f"Moved {file_name} to {category} folder.")

if __name__ == "__main__":
    # Set the path to your Downloads folder
    downloads_folder_path = "C:/Users/arzka/Downloads"

    organize_downloads(downloads_folder_path)