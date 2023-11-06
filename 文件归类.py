import os
import shutil
# import tkinter as tk
# from tkinter import filedialog

src_folder='/Users/ots/Desktop/School file/文档/成绩模版/学生数据 10月'

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# def get_new_name(file_path):
#     with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
#         content = file.read()
#     new_name = content[:3]
#     return new_name


def move_file(src_path, dest_folder):
    # 获取原始文件名和扩展名
    original_filename = os.path.basename(src_path) #basename函数可以去除路径，只保留路径上的文件名字
    # 构建目标路径
    dest_path = os.path.join(dest_folder, original_filename)
    # 移动文件
    shutil.move(src_path, dest_path)



def classify_files(src_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            src_path = os.path.join(root, file)
            # 获取文件的后缀名
            _, file_extension = os.path.splitext(src_path)
            # 检查文件后缀名是否为 .txt
            if file_extension.lower() == '.xlsx':
                dest_folder = os.path.join(src_folder, file[:3])  # 新文件夹名为文件的前三个字
                create_folder(dest_folder)
                move_file(src_path, dest_folder)
                print(dest_folder)

classify_files(src_folder)
# def select_folder():
#     src_folder = filedialog.askdirectory(title='Select Folder')
#     if src_folder:
#         classify_files(src_folder)




