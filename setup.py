# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='ebuynow',
    version=version,
    description='EBuy-Now',
    author='sagar.s@indictrasntech.com',
    author_email='sagar.s@indictrasntech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
