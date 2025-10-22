
'''Task: Write a script that prints all files in a directory and identifies which are files and which are folders.'''
# import os
# Step 1: Get list of items in the current directory
# items = os.listdir(".")

# # Step 2: Loop through items and print type (file/folder)
# for item in items:
#     # Your code here
#     if os.path.isfile(item):
#         print(f"{item} - file")
#     elif os.path.isdir(item):
#         print(f"{item} - folder")

'''Task: Create a folder named backup if it doesn’t exist, then list its contents.'''
# import os

# folder_name = "backup"

# # Step 1: Check if folder exists
# curr_path = os.path.join(".",folder_name)
# # Step 2: If not, create it
# if os.path.exists(curr_path):
#     print(os.listdir(curr_path))
# else:
#     os.mkdir(folder_name)
# Step 3: List contents

'''Task: Write a script that finds all .txt files in a directory and prints their full paths.'''

# Starter Template:

# import os

# directory = "."
# items = os.listdir(directory)
# for item in items:
#     # print(os.path.splitext(item))
#     if os.path.isfile(item) and os.path.splitext(item)[1] == '.txt':
#         print(f"{item} - {os.path.abspath(item)}")

# Step 1: List items in directory
# Step 2: Loop through and check extension
# Step 3: Print full path if .txt

'''Task: Write a script that recursively searches a directory for .log files older than 7 days and moves them to a logs_backup folder.'''
# import os
# import shutil
# import time

# source_dir = "."
# backup_dir = "logs_backup"

# Step 1: Ensure backup_dir exists
# Step 2: Walk through source_dir
# Step 3: Check if file ends with .log and older than 7 days
# Step 4: Move file to backup_dir

'''Task: Find all .log files recursively from current directory.'''

# import os

# for root, dirs, files in os.walk("."):
#     for file in files:
#         if os.path.splitext(file)[1] == ".log":
#             full_path = os.path.join(root, file)
#             print(os.path.abspath(full_path))

'''Task: Add _backup suffix to all .txt files in the current directory.'''

# import os

# for file in os.listdir("."):
#     if os.path.isfile(file) and os.path.splitext(file)[1] == ".txt":
#         name, ext = os.path.splitext(file)
#         new_name = f"{name}_backup{ext}"
#         os.rename(file, new_name)
#         print(f"Renamed: {file} → {new_name}")

    # Step 2: Rename to filename_backup.txt

