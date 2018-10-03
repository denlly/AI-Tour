

numpy.zeros_like
===================

::
    
numpy.zeros_like(a, dtype=None, order=&#39;K&#39;, subok=True)

summary
-------------

    Return an array of zeros with the same shape and type as a given array.

Parameters
----------------


-  **a** : array_like
    The shape and data-type of a define these same attributes ofthe returned array.  

-  **dtype** : data-type, optional
    Overrides the data type of the result.New in version 1.6.0.  

-  **order** : {‘C’, ‘F’, ‘A’, or ‘K’}, optional
    Overrides the memory layout of the result. ‘C’ means C-order,‘F’ means F-order, ‘A’ means ‘F’ if a is Fortran contiguous,‘C’ otherwise. ‘K’ means match the layout of a as closelyas possible.New in version 1.6.0.  

-  **subok** : bool, optional.
    If True, then the newly created array will use the sub-classtype of ‘a’, otherwise it will be a base-class array. Defaultsto True.  


return 
-----------

-  **out** : ndarray
    Array of zeros with the same shape and type as a.

note
----------

    当顺序为'A'且对象是既不是'C'也不是'F'顺序的数组，并且副本是由dtype的变化强制的，那么结果的顺序不一定是'C'，如预期的那样。这可能是一个错误。


examples
-----------





::

    >>> np.array([1, 2, 3])
    array([1, 2, 3])

Upcasting:

::
    >>> np.array([1, 2, 3.0])
    array([ 1.,  2.,  3.])


More than one dimension:

::

    >>> np.array([[1, 2], [3, 4]])
    array([[1, 2], [3, 4]])

Minimum dimensions 2:

::
    >>> np.array([1, 2, 3], ndmin=2)
    array([[1, 2, 3]])

Type provided:

::

    >>> np.array([1, 2, 3], dtype=complex)
    array([ 1.+0.j,  2.+0.j,  3.+0.j])

Data-type consisting of more than one element:

::
    >>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
    >>> x['a']
    array([1, 3])

Creating an array from sub-classes:

::
    >>> np.array(np.mat('1 2; 3 4'))
    array([[1, 2],
        [3, 4]])

::
    >>> np.array(np.mat('1 2; 3 4'), subok=True)
    matrix([[1, 2],
            [3, 4]])

see others
-------------

-  *empty_like* : Return an empty array with shape and type of input.

-  *ones_like* : Return an array of ones with shape and type of input.

-  *full_like* : Return a new array with shape of input filled with value.

-  *zeros* : Return a new array setting values to zero.
