#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:06:58 2021

@author: ayman
"""

from distutils.core import setup
from Cython.Build import cythonize


setup(ext_modules=cythonize('example_cy.pyx'))