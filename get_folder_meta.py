# -*- coding: utf-8 -*-
# Author: Bin-ze
# Email: binze.zero@gmail.com
# Date: 2024/8/23 11:23
# File Name: get_folder_meta.py

"""
Description of the script or module goes here.
构建本地的文件目录信息，上传云端尽心处理
直接保存为txt即可
"""
# Your code starts here
from pathlib import Path
import os

if __name__ == '__main__':

    root = "/Users/binze/Desktop/work_code/statistics_pcf/第一批数据"

    folder_tree_300 = [str(i) for i in Path(root).joinpath("300").rglob("*pdf")]
    folder_tree_150 = [str(i) for i in Path(root).joinpath("150").rglob("*pdf")]

    with open(os.path.join(root, "300dpi.txt"), 'w') as f:
        for i in folder_tree_300:
            f.write(i)
            f.write('\n')

    with open(os.path.join(root, "150dpi.txt"), 'w') as f:
        for i in folder_tree_150:
            f.write(i)
            f.write('\n')
