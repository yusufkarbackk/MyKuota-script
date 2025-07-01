import os
import shutil
import tempfile

# List of folders to delete
folders_to_delete = [
   "Code Cache",
   "Cache"
]

def remove_folders(profile_path):
    # Loop through the folders and delete them
    for folder in folders_to_delete:
        folder_path = os.path.join(profile_path, folder)
        if os.path.exists(folder_path):
            try:
                shutil.rmtree(folder_path)  # Recursively delete the folder and its contents
                #print(f"Deleted: {folder_path}")
            except Exception as e:
                with open(
                os.getenv('ERROR_REPORT_FILEI'), "a"
                ) as file:
                    file.write(f"{e}")
        else:
            with open(
                os.getenv('ERROR_REPORT_FILEI'), "a"
            ) as file:
                file.write("folder not found")