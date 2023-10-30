import os
import shutil

def add_numbered_prefix_to_folders(path, start_num=200):
    count = 0
    with open('counter.txt', 'r') as f:
        last_count = int(f.read())
    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path):
            count += 1
            if count > last_count:
                new_folder_name = f"{start_num+count:04d}" + folder
                new_folder_path = os.path.join(path, new_folder_name)
                os.rename(folder_path, new_folder_path)
    with open('counter.txt', 'w') as f:
        f.write(str(count))

# 指定文件夹路径和起始编号
folder_path = './'
start_num = 200

# 读取文件夹数量并添加数字前缀到文件夹
add_numbered_prefix_to_folders(folder_path, start_num)
