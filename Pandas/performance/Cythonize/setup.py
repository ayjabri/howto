#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup with Numpy:
--------------
To successfully complie Cython script with numpy function in it
you must include numpy directory.
Get the directory path using np.get_include()

In summary, to compile Cython with Numpy:
    1- import numpy in the setup file
    2- add: include_dir=[np.get_include()] in your setup



@author: Ayman Al Jabri
"""

from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name='Demon Cython with Numpy Arrays',
    ext_modules=cythonize("myfunc.pyx"),
    zip_safe=False,
    include_dirs=[np.get_include()]
    
)
