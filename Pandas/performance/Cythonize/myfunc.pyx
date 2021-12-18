#
import numpy as np
cimport numpy as np
cimport cython

DTYPE='float64'


cdef double f_cy(double x):
    return x * (x-1)


cdef double integrate_f_cy(double a,double b, int N):
    cdef double s = 0.
    cdef double dx = (b-a)/N
    cdef int i = 0
    for i in range(N):
        s += f_cy(a + i * dx)
    return s * dx

@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
cpdef compute(double[:] col_a,double[:] col_b,long[:] col_N):
    #First define the memeory view index for 1D array as dtype[:], 2D array as dtype[:,:]..and so on
    cdef Py_ssize_t a_size = col_a.shape[0]
    # define the size of the array as Py_ssize_t (standard size object)
    
#     assert col_a.shape == col_b.shape == col_N.shape
#     assert col_a.dtype == col_b.dtype == DTYPE
    # assert that the sizes and datatypes are correct
    
    results = np.zeros((a_size,), dtype=DTYPE)
    # define an empty array to host your calculations
    
    cdef double[:] results_view = results
    # define a memory view fo the results: dtype[:] if your resutls are one array
    cdef Py_ssize_t i
    for i in range(a_size):
        results_view[i] = integrate_f_cy(col_a[i],col_b[i],col_N[i])
    return results