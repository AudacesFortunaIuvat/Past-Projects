#This is a concise program was born out of the need to prep a large, disorganized dataset for review by the IRB's
#of the university of Rochester, Dublin, and BYU. The code systematically iterates over a disjointed dataset of
#hundreds of weeks of data, grabbing folders that fit certain naming criteria, and moving them into a new unified
#directory, with easily navigable folder structure.

import os
import shutil

#set source directory
src_dir = r"C:\Users\grega\Box\Audio Data for IRB\Recordings Winter 2021"
dir_ranges = [(401, 408), (501, 516), (601, 610), (701, 709)]

for start, end in dir_ranges:
    for i in range(start, end):
        old_dir_path = os.path.join(src_dir, str(i))
        for j in range(3, 14):
            week_dir = "week " + str(j)
            week_dir_path = os.path.join(old_dir_path, week_dir)
            #checking if the week directory exists in the old directory
            if os.path.exists(week_dir_path):
                new_dir_path = os.path.join(src_dir, week_dir, str(i))
                #creating new directories if they don't exist
                os.makedirs(new_dir_path, exist_ok=True)
                #moving the files
                for file_name in os.listdir(week_dir_path):
                    shutil.move(os.path.join(week_dir_path, file_name), new_dir_path)
