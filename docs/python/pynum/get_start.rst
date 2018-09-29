快速开始
==========

先决条件
----------

    1. 首先安装Python，目前老夫当前的版本是python3.7。
    2. 已安装 NumPy 

基本用法
--------

NumPy的主要对象是同构多维数组。它是一个元素表（通常是数字），都是相同的类型，由正整数元组索引。在NumPy维度中称为 *axes*。例如，3D空间[1,2,1]中的点的坐标具有一个 *axes* 。 该axes有3个元素，所以我们说它的长度为3.在下图所示的例子中，数组有2个 *axes*。 第一 *axes* 的长度为2，第二 *axes* 的长度为3。
NumPy的数组类称为ndarray。 它也被别名数组所知。 请注意，numpy.array与标准Python库类array.array不同，后者仅处理一维数组并提供较少的功能。 ndarray对象的更重要的属性是：

ndarray.ndim(ndarray)    
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    **获取阵列的 *axes* 数**

:: 

    nd1 = ([0,  1,  2,  3])
    nd2 = ([[0,  1,  2,  3],
            [4,  5,  6,  7],
            [8,  9, 10, 11]])
    nd3 = ([[[0,  1,  2,  3],
            [4,  5,  6,  7],
            [8,  9, 10, 11]],
            [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])
    print(np.ndim(nd1))  // 1
    print(np.ndim(nd2))  // 2
    print(np.ndim(nd3))  // 3 


ndarray.shape(ndarray)
>>>>>>>>>>>>>>>>>>>>>>>>>>

    **数组的大小。这是一个整数元组，表示每个维度中数组的大小。对于具有n行和m列的矩阵，形状将为（n，m）。因此，形状元组的长度是 *axes* 的数量ndim。**

:: 

    import numpy as np

    nd1 = ([0,  1,  2,  3])
    nd2 = ([[0,  1,  2,  3],
            [4,  5,  6,  7],
            [8,  9, 10, 11]])
    nd3 = ([[[0,  1,  2,  3],
            [4,  5,  6,  7],
            [8,  9, 10, 11]],
            [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])

    print(np.shape(nd1))        #(4,)
    print(np.shape(nd2))        #(3, 4)
    print(np.shape(nd3))        #(2, 3, 4)


ndarray.size(ndarray)
>>>>>>>>>>>>>>>>
    
    **数组的元素总数。这等于 m * n 个元素。**

:: 

    import numpy as np

    nd1 = ([0,  1,  2,  3])
    nd2 = ([[0,  1,  2,  3],
            [4,  5,  6,  7],
            [8,  9, 10, 11]])
    nd3 = ([[[0,  1,  2,  3],
            [4,  5,  6,  7],
            [8,  9, 10, 11]],
            [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])

    print(np.size(nd1))  # 1 X 4  = 4
    print(np.size(nd2))  # 3 X 4  = 12 
    print(np.size(nd3))  # 2 X 3 X 4  = 24


ndarray.dtype
>>>>>>>>>>>>>>>>

    **描述数组中元素类型的对象。可以使用标准Python类型创建或指定dtype。此外，NumPy还提供自己的类型。 numpy.int32，numpy.int16和numpy.float64就是一些例子。** 

    TODO

ndarray.itemsize
>>>>>>>>>>>>>>>>>>>

    **数组中每个元素的大小（以字节为单位）。例如，float64类型的元素数组具有itemsize 8（= 64/8），而complex32类型之一具有itemsize 4（= 32/8）。它相当于ndarray.dtype.itemsize**
    
    TODO

ndarray.data
>>>>>>>>>>>>>>>

    **包含数组实际元素的缓冲区。通常，我们不需要使用此属性，因为我们将使用索引工具访问数组中的元素。**

    TODO

numpy.array(array)
>>>>>>>>>>>>>>>>
    
    **您可以使用数组函数从常规Python列表或元组创建数组。结果数组的类型是从序列中元素的类型推导出来的。**

numpy.zeros(tuple, options?)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


numpy.ones(tuple, options?)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


numpy.empty(tuple, options?)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


numpy.arange(beginNumber,endNumber,stepLenght)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    - beginNumber: 数字范围的开始数
    - endNumber: 数字方位的结束数（不包含）
    - stepLength：后数 - 前数 = stepLength

numpy.linspace()
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

numpy.reshape()
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

数据运算
----------------

+ - * / @ ^ 


索引，切片，迭代
-------------------


矩阵形状操作
---------------

Changing the shape of an array

Stacking together different arrays¶

Splitting one array into several smaller ones

拷贝 & 视图
-----------------

No Copy at All

View or Shallow Copy

Deep Copy


Functions and Methods Overview
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Here is a list of some useful NumPy functions and methods names ordered in categories. See Routines for the full list.

Array Creation
arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like
Conversions
ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat
Manipulations
array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
Questions
all, any, nonzero, where
Ordering
argmax, argmin, argsort, max, min, ptp, searchsorted, sort
Operations
choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum
Basic Statistics
cov, mean, std, var
Basic Linear Algebra
cross, dot, outer, linalg.svd, vdot

广播规则
--------------

    | 广播允许通用功能以有意义的方式处理不具有完全相同形状的输入。
    | 
    | 规则一：如果所有输入数组不具有相同数量的维度，则将“1”重复地预先添加到较小阵列的形状，直到所有阵列具有相同数量的维度。
    | 
    | 规则二：确保沿着特定维度的大小为1的数组就好像它们具有沿着该维度具有最大形状的阵列的大小。 假定数组元素的值沿着“广播”数组的那个维度是相同的。
    |
    | 应用广播规则后，所有阵列的大小必须匹配。 更多细节可以在广播中找到。

脑花缭乱的索引
---------------

Fancy indexing and index tricks

Indexing with Boolean Arrays


线性代数
-------------

Linear Algebra


奇技in巧
-------------

“Automatic” Reshaping

Vector Stacking

Histograms