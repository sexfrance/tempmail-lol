from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(name='tempmail-lol2',
      version='3.0.0',
      description='A Python API for TempMail with rate limit bypassing',
      author='Alexander Epolite, Alex Torres, Sexfrance',
      author_email='contact@bananacrumbs.us',
      url="https://github.com/sexfrance/tempmail-lol",
      maintainer='Sexfrance',
      maintainer_email="bwuuuuu@gmail.com",
      packages=find_packages(),
      install_requires=['requests'],
      keywords=['tempmail', 'api', 'lol', 'tempmail-lol', 'tempmail.lol', 'email', 'free', 'tempmail-lol-bypass', 'rate-limit-bypass'],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ]
    )
