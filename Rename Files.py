import os
def rename_files():
    # 1, Get file names from a folder.
    file_list = os.listdir(r"E:\Udacity\P3\prank\prank")
    print file_list
    os.chdir(r"E:\Udacity\P3\prank\prank")
    # 2, For each file, rename filename.
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, '0123456789'))

rename_files()
