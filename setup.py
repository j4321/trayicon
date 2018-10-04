from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='trayicon',
      version='0.1.0',
      description='Multi-GUI-toolkit system tray icon package for use with a Tkinter main GUI',
      long_description=long_description,
      url='https://github.com/j4321/trayicon',
      author='Juliette Monsel',
      author_email='j_4321@protonmail.com',
      license='GPLv3',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Topic :: Software Development :: Widget Sets',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Operating System :: Linux'],
      keywords=['tkinter', 'system-tray',],
      py_modules=["trayicon.qticon",
                  "trayicon.tkicon",
                  "trayicon.gtkicon"],
      packages=["trayicon"])
      package_data=[{"trayicon": "packages.tcl"}])
