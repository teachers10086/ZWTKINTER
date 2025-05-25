# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# 读取 README.md 文件作为 long_description
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="ZWTKINTER",  
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow",
    ],
    author="Liuyuming",
    author_email="1571528072@qq.com",
    description="一个简化的中文 Tkinter GUI 组件库",
    long_description=long_description,  # 添加 long_description
    long_description_content_type="text/markdown",  # 指定内容类型为 Markdown
    url="https://github.com/teachers10086/ZWTKINTER",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
