import os
import shutil
import stat
from dotenv import load_dotenv

load_dotenv()


def on_rm_error(func, path, exc_info):
    # Change permission and retry
    os.chmod(path, stat.S_IWRITE)
    func(path)

def remove_profile(profile_path):
    folder_path = os.path.abspath(profile_path)

    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path, onerror=on_rm_error)
        except Exception as e:
            log_error(f"Error deleting folder '{folder_path}': {e}")
    else:
        log_error(f"Folder not found: {folder_path}")

def log_error(message):
    error_file = os.getenv('ERROR_REPORT_FILE')
    if error_file:
        with open(error_file, "a") as file:
            file.write(message + "\n")
    else:
        print(message)
