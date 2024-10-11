import os
import shutil

def compare_folders(big_folder, little_folder):
    """
    Compares two folders and removes duplicate files from the big folder.

    Args:
        big_folder: The path to the larger folder.
        little_folder: The path to the smaller folder.
    """

    # Get a list of files in each folder
    big_files = os.listdir(big_folder)
    little_files = os.listdir(little_folder)

    # Iterate through the files in the smaller folder
    for file in little_files:
        # If the file exists in the larger folder, delete it
        if file in big_files:
            big_file_path = os.path.join(big_folder, file)
            os.remove(big_file_path)
            print(f"Removed duplicate file: {file}")

# Example usage
big_folder = r"path/to/your/files"
little_folder = r"path/to/your/files"

compare_folders(big_folder, little_folder)