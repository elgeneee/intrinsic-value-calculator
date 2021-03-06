"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Intrinsic.py']
DATA_FILES = ['backend.py']
OPTIONS = {
    'iconfile':'intrinsic_logo.icns',
    'argv_emulation':True,
    'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
