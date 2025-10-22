'''File Organizer Bot → sort files into folders
sys-arg - take current path as param for folder path.
recursively loop through files in directory
--> check for the file extension (txt/pdf/json/py/xlsx/ods/csv) :
--> alternatively iterate over the files and get their extensions
 and store as a list.
Then accordingly create folders with extension type as folder name
in the main directory path, not in child dir.
agan iterate over the files to move as per their ext. type
either give single file path or multiple paths to organise as list. and organise 1 path at a time.
integrate to github, jenkins.Trigger, overview results

'''
from pathlib import Path
import os
# import sys
import shutil

FOLDER_PATH = r"C:\\Users\\12187\Downloads\Automation\Androidauto\\auto_path_SU\\New_folder"
path_list = []
#
# if (len(sys.argv) == 1): #if only script name is taken passed as arg
#     folder_path = Path.cwd()
# elif len(sys.argv) == 2:
#     folder_path = sys.argv[1:]
# else:
#     for i in range(1,len(sys.argv)+1):
#         path_list.append(sys.argv[i])
#         print("Check for the following paths: ", path_list)

def sort_files_to_folder(folder_path):
    '''

    :param folder_path: dir path that needs to be organised
    :return: files sorted based on extension format
     moved to folder with foldername as extension format respectively
    '''
    print("folder path : ",folder_path)
    valid_file_ext = []
    # curr_dir = Path.cwd()
    # print("curr_dir",curr_dir)
    for file in Path(folder_path).rglob('*'):
        print(file)

        extension = Path(file).suffix
        dir_path = os.path.join(folder_path,extension)
        # Check if the directory exists
        if os.path.isdir(dir_path):
            print("Directory exists - ",dir_path)
        else:
            print("Directory does not exist - ",dir_path)
            os.mkdir(dir_path)
        if extension not in valid_file_ext:
            valid_file_ext.append(extension)
            file_name = os.path.basename(file)
            shutil.move(file, dir_path + "\\"+ file_name)
            print("Moved file : ",file)
        else:
            file_name = os.path.basename(file)
            shutil.move(file, dir_path + "\\" + file_name)
            print("Moved file : ", file)

    # for exten in valid_file_ext:
    #     dir_name = exten
    #     os.mkdir(dir_name)
    # for file in Path(folder_path).rglob('*'):
    #     check_ext = Path(file).suffix
    #     if check_ext in valid_file_ext:
    #         shutil.move(file,dir_name )

sort_files_to_folder(folder_path = FOLDER_PATH)

# if path_list:
#     for i in range(len(path_list)):
#         folder_path = path_list[i]
#         sort_files_to_folder(folder_path)
# else:
#     sort_files_to_folder(folder_path)
