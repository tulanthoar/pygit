"""build script for click apps (console scripts)"""
from setuptools import setup

setup(
    name='flighttimes',
    version='0.1',
    py_modules=['flighttimes'],
    install_requires=[
        'Click',
        'beautifulsoup4',
        'requests',
        'colorama',
        'termcolor',
    ],
    entry_points='''
        [console_scripts]
        flighttimes=flighttimes:text_loop
    ''',
)
