numpy.array
===================

..code ::

    numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

summary
-------------

.. note:: 
    创建一个 array

Parameters
----------------

    object ： array_like
数组，公开数组接口的任何对象，__array__方法返回数组的对象，或任何（嵌套）序列。

dtype ： 数据类型，可选
数组所需的数据类型。如果没有给出，那么类型将被确定为保持序列中的对象所需的最小类型。此参数只能用于“upcast”数组。对于向下转换，请使用.astype（t）方法。

copy ： bool，可选
如果为true（默认值），则复制对象。否则，仅当__array__返回副本，obj是嵌套序列，或者需要副本以满足任何其他要求（dtype，顺序等）时，才会生成副本。

顺序 ： {'K'，'A'，'C'，'F'}，可选
指定阵列的内存布局。如果object不是数组，则新创建的数组将按C顺序排列（行主要），除非指定了“F”，在这种情况下，它将采用Fortran顺序（专业列）。如果object是一个数组，则以下成立。

订购	没有副本	复制=真
'K'	不变	F＆C订单保留，否则最相似的订单
'一个'	不变	如果输入为F而不是C，则为F顺序，否则为C顺序
'C'	C命令	C命令
'F'	F订单	F订单
当copy=False出于其他原因而复制时，结果copy=True与对A的一些例外情况相同，请参阅“注释”部分。默认顺序为“K”。

subok ： bool，可选
如果为True，则子类将被传递，否则返回的数组将被强制为基类数组（默认）。

ndmin ： int，可选
指定结果数组应具有的最小维数。为满足此要求，将根据需要预先设置形状。

return 
-----------

    ndarray
    满足指定要求的数组对象。

example
-----------

.. code::

    >>> np.array([1, 2, 3])
    array([1, 2, 3])