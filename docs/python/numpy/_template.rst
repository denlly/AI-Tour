{% import tornado %}
{{ data.title }}
===================

::

    {{ tornado.escape.xhtml_unescape(data.method) }}

summary
-------------

    {{ data.summary }}

Parameters
----------------

{% for param in data.params %}
-  **{{ param.name }}** : {{ param.type }}
    {{ param.desc }}
    {{ param.notice }}
{% end %}

-  **object**: array_like 
    数组，公开数组接口的任何对象，__array__方法返回数组的对象，或任何（嵌套）序列。

-  **dtype**: data-type, optional
    数组所需的data-type。如果没有给出，那么类型将被确定为保持序列中的对象所需的最小类型。此参数只能用于‘upcast’数组。对于向下转换，请使用 .astype(t)方法。

- **copy**: bool, optional
    如果为True（默认值），则复制对象。否则，仅当__array__返回副本，obj是嵌套序列，或者需要副本以满足任何其他要求(dtype, order.)时，才会生成副本。

- **order**: {‘K’, ‘A’, ‘C’, ‘F’}, optional
    指定阵列的内存布局。如果object不是数组，则新创建的数组将按C顺序排列（行主要），除非指定了“F”，在这种情况下，它将采用Fortran顺序（专业列）。如果object是一个数组，则以下成立。
    order	no copy	copy=True
    ‘K’	unchanged	F & C order preserved, otherwise most similar order
    ‘A’	unchanged	F order if input is F and not C, otherwise C order
    ‘C’	C order	C order
    ‘F’	F order	F order

- **subok**: bool, optional
    如果为True，则子类将被传递，否则返回的数组将被强制为基类数组（默认）。

- **ndmin**: int, optional
    指定结果数组应具有的最小维数。为满足此要求，将根据需要预先设置形状。


return 
-----------

    ndarray
    满足指定要求的数组对象。

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

    empty_like
    Return an empty array with shape and type of input.
    ones_like
    Return an array of ones with shape and type of input.
    zeros_like
    Return an array of zeros with shape and type of input.
    full_like
    Return a new array with shape of input filled with value.
    empty
    Return a new uninitialized array.
    ones
    Return a new array setting values to one.
    zeros
    Return a new array setting values to zero.
    full
    Return a new array of given shape filled with value.