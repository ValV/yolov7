from pathlib import Path
from setuptools import setup

package = 'yolov7'
packages = [package] + [str(path) for path in Path(package).rglob('*/')
                        if path.is_dir() and '__' not in str(path)]

setup(
    name='yolov7',
    version='0.1.0',
    package_data={
        '': ['*.yaml'],
    },
    packages=packages,
    url='https://github.com/ValV/yolov7',
    license='GPLv3',
    author='ValV',
    author_email='0x05a4@gmail.com',
    description='YOLOv7 core package',
    install_requires=[
    ]
)