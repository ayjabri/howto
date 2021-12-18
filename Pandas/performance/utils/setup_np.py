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


Created on Mon Dec  6 09:41:24 2021

@author: ayman
"""
import numpy as np
from distutils.core import setup
from Cython.Build import cythonize


setup(
      ext_modules=cythonize('myfunc_np.pyx'),
      include_dirs=[np.get_include()]
      )