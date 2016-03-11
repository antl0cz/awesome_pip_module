import re
from setuptools import setup


version = re.search(
   '^__version__\s*=\s*"(.*)"',
   open('new_html/new_html.py').read(),
   re.M
   ).group(1)


with open("README.rst", "rb") as f:
   long_descr = f.read().decode("utf-8")


setup(
   name = "awesome_pip_module",
   packages = ["awesome_pip_module"],
   entry_points = {
       "console_scripts": ['awesome_pip = awesome_pip_module.awesome_module:awesome_module']
       },
   version = version,
   description = "Python command line html creator",
   long_description = long_descr,
   author = "Anthony Nguyen",
   author_email = "phuanthony.nguyen@gmail.com",
   url = "https://github.com/antl0cz/awesome_pip_module.git")
