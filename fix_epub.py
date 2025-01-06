import zipfile
import os
from bs4 import BeautifulSoup

def fix_html_tags_in_epub(epub_path):
    # 创建一个临时目录来解压 EPUB 文件
    temp_dir = 'temp_epub'
    with zipfile.ZipFile(epub_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    # 遍历解压后的文件
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            if file.endswith('.html') or file.endswith('.xhtml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 使用 BeautifulSoup 解析 HTML
                soup = BeautifulSoup(content, 'lxml')

                # 查找所有 img 标签并确保它们是自闭合的
                for img in soup.find_all('img'):
                    img_tag = str(img)
                    if not img_tag.endswith('/>'):
                        img.insert_before(soup.new_tag('img', src=img['src'], alt=img.get('alt', ''), **{'self-closing': True}))
                        img.decompose()  # 删除原来的 img 标签

                # 保存修改后的 HTML 文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))

    # 重新打包为 EPUB 文件，替换原文件
    with zipfile.ZipFile(epub_path, 'w') as zip_ref:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, temp_dir))

    # 清理临时目录
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_dir)

    print(f"修复完成，已替换原 EPUB 文件: {epub_path}")

def fix_all_epubs_in_current_folder():
    current_folder = os.getcwd()  # 获取当前工作目录
    for file in os.listdir(current_folder):
        if file.endswith('.epub'):
            epub_path = os.path.join(current_folder, file)
            print(f"正在修复: {epub_path}")
            fix_html_tags_in_epub(epub_path)

# 使用示例
fix_all_epubs_in_current_folder()