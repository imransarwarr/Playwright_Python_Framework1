import os

AUTH_FILE = ".auth/user.json"

def auth_file_exists():
    return os.path.exists(AUTH_FILE)