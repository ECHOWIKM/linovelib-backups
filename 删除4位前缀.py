import os

# 指定要遍历的根目录
rootdir = './'

# 定义要删除的前缀长度
prefix_length = 4

# 遍历根目录下所有文件夹
for subdir, dirs, files in os.walk(rootdir):
    for dir_name in dirs:
        # 获取文件夹的完整路径
        dir_path = os.path.join(subdir, dir_name)
        # 获取原始文件夹名称
        original_name = os.path.basename(dir_path)
        
        # 检查文件夹名称是否符合指定规律
        if len(original_name) >= prefix_length and original_name[:prefix_length].isdigit():
            # 删除前缀
            new_dir_name = original_name[prefix_length:]
            # 生成新的文件夹路径，并重命名
            new_dir_path = os.path.join(subdir, new_dir_name)
            os.rename(dir_path, new_dir_path)
            print(f"已将文件夹 {original_name} 重命名为 {new_dir_name}")
