# Backup automation

import os
from tkinter.filedialog import askdirectory
import shutil
import datetime

select_folder = askdirectory()

file_list = os.listdir(select_folder)
current_date = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")

backup_name = "backup"
backup_name_file = f"{select_folder}/{backup_name}"

for file in file_list:
    file_name = f"{select_folder}/{file}"
    file_name_final = f"{backup_name_file}/{current_date}/{file}"
    if "." in file:
        shutil.copy2(file_name, file_name_final)
    elif "backup" != file:
        shutil.copytree(file_name, file_name_final)

print(f"The {backup_name} {current_date} has been completed.")