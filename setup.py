from setuptools import setup
import os.path
import sys

setup(
    name='pysetupdi',
    version='2018.10.22',
    packages=['pysetupdi'],
    url='https://github.com/gwangyi/pysetupdi',
    license='MIT',
    author='Sungkwang Lee',
    author_email='gwangyi.kr@gmail.com',
    description='Python SetupAPI wrapper',
    platforms=['win32'],
    entry_points={
        'console_scripts': ['pysetupdi=pysetupdi.__main__:main']
    }
)
