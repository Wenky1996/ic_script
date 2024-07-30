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
file_list = open("rtl.f",'w+')

for root,dir,files in os.walk(current_folder):
    file_type = os.path.splitext(files)[1]
    

def __main__():
    print("")
