#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Objective:
----

Compare the speed of a function in two languanges; Cython vs. Python.

The function is in:
    1- example.py
    2- example_cy.cpython-39-...

To run this you must first compile the function in example_cy.pyx

Test steps:
----
Generate 'n' sized pandas dataframe, apply the function to it
    and print out the ratio of python/cython.

If the ratio > 1 => Cython is faster by x


Created on Sun Dec  5 14:53:27 2021

@author: ayman
"""
import example_cy
import example

import pandas as pd
import numpy as np
import time


n = 100_000

data = {'a':np.random.randn(n),
   'b':np.random.randn(n),
   'N':np.random.randint(100,1000, (n,)),
   'x': 'x'}

df = pd.DataFrame(data)

start = time.time()
df.apply(lambda x: example_cy.integrate_f(x['a'],x['b'],x['N']), axis=1)
cy_time = time.time() - start

start = time.time()
df.apply(lambda x: example.integrate_f(x['a'],x['b'],x['N']), axis=1)
py_time = time.time() - start


faster = py_time/cy_time
print(f'Cython is {faster:.3f} faster than python')