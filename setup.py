from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='foxtrotli_co',
    version=version,
    description='FoxtrotLI.co',
    author='Brandon Fox',
    author_email='bfox@foxtrot.email',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
