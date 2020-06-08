import os
import shutil
import sys

from setuptools import setup, find_packages

package_name = 'pynq-memes'

notebook_source_folder = 'notebook/'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']


setup(
    name=package_name,
    version='0.1',
    description='Face detection and meme generation',
    author='PYNQ Hero',
    url='https://github.com/riklaunim/pynq-meme-generator',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "pynq",
        "pluggy>=0.13.1",
        "pytest>=5.4.3",
        "ipytest>=0.8.1",
    ],
)


def install_notebook(notebook_name):
    notebook_path = os.path.join(board_notebooks_dir, notebook_name)
    if os.path.isdir(notebook_path):
        shutil.rmtree(notebook_path)
    shutil.copytree(notebook_source_folder, notebook_path)


if 'install' in sys.argv:
    install_notebook(package_name)
