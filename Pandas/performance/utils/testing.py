#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Objective:
----

Compare the speed of the compiled Cython vs. Python function found in:
    1- example.py
    2- example_cy.cpython-39-...

To run this you must first compile the function in example_cy.pyx


Created on Sun Dec  5 14:05:44 2021

@author: ayman
"""

import timeit


n = 10000 # Number of time time to run timeit

cy_time = timeit.timeit('example_cy.integrate_f(10, 5 , 1000)', setup='import example_cy', number=n)
py_time = timeit.timeit('example.integrate_f(10,5,1000)', setup='import example', number=n)


faster = py_time/cy_time
print(f'Cython is {faster:.3f} faster than python')
