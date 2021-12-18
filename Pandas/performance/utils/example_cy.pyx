#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:06:22 2021

@author: ayman
"""

cdef float f(float x):
    return x * (x - 1)


cpdef float integrate_f(float a,float b,int N):
    cdef float s = 0.0, dx = (b-a)/N
    cdef int i
    # cdef float dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx