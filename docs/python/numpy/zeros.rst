numpy.zeros¶
===================

::

    numpy.zeros(shape, dtype=float, order='C')

summary
-------------

    numpy.zeros(shape, dtype=float, order='C')¶

Parameters
----------------

-   **shape**: int or tuple of ints
        Shape of the new array, e.g., (2, 3) or 2.

-   **dtype**: data-type, optional
        The desired data-type for the array, e.g., numpy.int8. Default is numpy.float64.

-   **order**: {‘C’, ‘F’}, optional, default: ‘C’
        Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.
  
return 
-----------
    out : ndarray
        Array of zeros with the given shape, dtype, and order.

example
-----------

::

    >>> np.zeros(5)
    array([ 0.,  0.,  0.,  0.,  0.])

::

    >>> np.zeros((5,), dtype=int)
    array([0, 0, 0, 0, 0])

::

    >>> np.zeros((2, 1))
    array([[ 0.],
        [ 0.]])

::

    >>> s = (2,2)
    >>> np.zeros(s)
    array([[ 0.,  0.],
        [ 0.,  0.]])

::

    >>> np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
    array([(0, 0), (0, 0)],
        dtype=[('x', '<i4'), ('y', '<i4')])

see others
-------------

zeros_like
Return an array of zeros with shape and type of input.
empty
Return a new uninitialized array.
ones
Return a new array setting values to one.
full
Return a new array of given shape filled with value.
