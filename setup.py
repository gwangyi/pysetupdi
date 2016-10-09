from setuptools import setup
import pathlib
import os.path
import sys

setup(
    name='pysetupdi',
    version='2016.10.9',
    packages=['pysetupdi'],
    url='https://github.com/gwangyi/pysetupdi',
    license='MIT',
    author='Sungkwang Lee',
    author_email='gwangyi.kr@gmail.com',
    description='Python SetupAPI wrapper',
    platforms=['win32'],
    data_files=[
        (
            'shared/typehints/python{}.{}'.format(*sys.version_info[:2]),
            iter(str(path) for path in pathlib.Path(os.path.dirname(__file__)).glob('**/*.pyi')),
        ),
    ],
    entry_points={
        'console_scripts': ['pysetupdi=pysetupdi.__main__:main']
    }
)
