# -----------------------------------------------------------------------------
# Copyright (c) 1996-2024 All rights reserved
# -----------------------------------------------------------------------------
# Author : Wenky
# File   : filelist.py
# Email  : wenkyjong1996@gmail.com
# Create : 2024-07-14
# Project: ic_script
# Functions : Create Filelist

import os

current_folder = os.getcwd()

with open("rtl.f",'w') as file_list:
    for root,dir,files in os.walk(current_folder):
        for file in files:
            file_type = os.path.splitext(file)[1]
            if file_type == ".v" or file_type == ".sv" or file_type == ".h" or file_type == ".vh":
                print(root)
                print(file)
                file_list.write(root+'/'+file+"\n")
            else:
                continue

print("filelist created ")
