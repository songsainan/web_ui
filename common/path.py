import os

file_path = os.path.abspath(__file__)
file_dir = os.path.dirname(file_path)
base_dir = os.path.dirname(file_dir)

LOG_DIR = os.path.join(base_dir, 'logs')
ERROR_IMG_DIR = os.path.join(base_dir, 'error_img')
