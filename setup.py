#-*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
setup(
    name='django-dbbackupyandexdisk',
    version='0.0.2',
    include_package_data=True,
    py_modules=['dbbackupyandexdisk'],
    url='https://github.com/lexich/django-dbbackupyandexdisk',
    license='BSD',
    author='lexich',
    author_email='lexich121@gmail.com',
    description='Storage yandex-disk for django-dbbackup',
    long_description=README,
    install_requires=[
        "django",
        "django-dbbackup",
        "yandexwebdav"
    ]
)
