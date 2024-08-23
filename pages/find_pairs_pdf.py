# -*- coding: utf-8 -*-
# Author: Bin-ze
# Email: binze.zero@gmail.com
# Date: 2024/8/20 16:15
# File Name: find_pairs_pdf.py

"""
Description of the script or module goes here.
检查300 与 150的对应关系
"""
# Your code starts here
from pathlib import Path
import pandas as pd
import streamlit as st

class find_pairs_pdf:
    def __init__(self, txt_300dpi, txt_150_dpi):

        self.book_300 = self.decode_txt(txt_300dpi)
        self.book_150 = self.decode_txt(txt_150_dpi)

    # def decode_txt(self, txt):
    #     with open(txt, 'r') as f:
    #         meta = f.readlines()
    #
    #     return  [Path(i.splitlines()[0]) for i in meta]

    def decode_txt(self, uploaded_file):
        # 直接读取 UploadedFile 对象的内容
        content = uploaded_file.getvalue().decode("utf-8")
        meta = content.splitlines()

        return [Path(line) for line in meta]

    def query_exist(self):
        error_300 = []
        error_150 = []
        for i in self.book_150:
            # 为了300不在文件名中出现，需要添加额外逻辑
            path_300_pdf = Path(str(i.parent.parent).replace("150", "300")) / i.parent.name / i.name
            if path_300_pdf not in self.book_300:
                error_300.append(str(path_300_pdf))

        for i in self.book_300:
            # 为了300不在文件名中出现，需要添加额外逻辑
            path_150_pdf = Path(str(i.parent.parent).replace("300", "150")) / i.parent.name / i.name
            if path_150_pdf not in self.book_150:
                error_150.append(str(path_150_pdf))

        return error_150, error_300

    def __call__(self, *args, **kwargs):
        error_150, error_300 = self.query_exist()
        # print(error_300, error_150)
        return error_300, error_150

def main():
    st.set_page_config(page_title="300dpi与150dpi文件对照工具", page_icon="📈")
    st.markdown("# 300dpi与150dpi文件对照工具")
    st.sidebar.header("300dpi与150dpi文件对照工具")
    st.write(
        """该工具用于验证300dpi文件与150dpi文件是否对照"""
    )

    txt_300_dpi = st.file_uploader("上传300 dpi txt", type=["txt"])
    txt_150_dpi = st.file_uploader("上传150 dpi txt", type=["txt"])

    if txt_300_dpi and txt_150_dpi:
        is_disabled = st.session_state.get('is_disabled', False)

        if st.button("执行检查", disabled=is_disabled):
            st.session_state.is_disabled = True
            with st.spinner('检查中，请稍候...'):
                pdf_check = find_pairs_pdf(txt_300_dpi, txt_150_dpi)
                error_300, error_150 = pdf_check()
                st.success("检查完成！")
                st.session_state.is_disabled = False

                if (error_150 == [] and error_300 == []):
                    st.write("检查通过，未发现不对应的文件")
                else:
                    # 显示不对应的结果
                    if error_300:
                        st.write("未找到对应的300 dpi文件：")
                        error_300_df = pd.DataFrame(error_300, columns=["未找到对应的300 dpi文件"])
                        st.dataframe(error_300_df)

                    if error_150:
                        st.write("未找到对应的150 dpi文件：")
                        error_150_df = pd.DataFrame(error_150, columns=["未找到对应的150 dpi文件"])
                        st.dataframe(error_150_df)

if __name__ == '__main__':
    main()
    # txt_300dpi, txt_150_dpi = '/Users/binze/Desktop/work_code/statistics_pcf/第一批数据/300dpi.txt',\
    #                         '/Users/binze/Desktop/work_code/statistics_pcf/第一批数据/150dpi.txt'
    #
    # pdf_check = find_pairs_pdf(txt_300dpi, txt_150_dpi)