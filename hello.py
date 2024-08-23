# -*- coding: utf-8 -*-
# Author: Bin-ze
# Email: binze.zero@gmail.com
# Date: 2024/8/23 16:24
# File Name: hello.py.py

"""
Description of the script or module goes here.
"""

# Your code starts here
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    这是一个用于检查期刊和数据库格式是否对应的应用
    ## find_pairs_pdf: 
        用于检查300和150两个文件夹下的文件是否是一一对应的，由于远程无法访问本地文件夹，需要上传包含两个文件下pdf路径的txt文件
    ## xlsx_check:
        用于检查xlsx文件是否满足格式要求，比如是否存在错误的大小写，是否没有补全期名等
    ## error_data_statistics：
        用于检查xlsx文件中包含的期刊索引与数据库路径下的文件的对应关系，并标记当前匹配和错误。需要上传xlsx和一个包含数据库pdf绝对路径的txt文件，如find_pairs_pdf中用到的
    """
)