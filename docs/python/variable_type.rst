变量类型
==========

变量只是用于存储值的保留内存位置。这意味着当您创建变量时，您在内存中保留了一些空间。
根据变量的数据类型，解释器分配内存并决定可以存储在保留内存中的内容。因此，通过为变量分配不同的数据类型，可以在这些变量中存储整数，小数或字符。

赋值-常规版
~~~~~~~~~~~~~~~~~
:: 

    #!/usr/bin/python

    counter = 100          # An integer assignment
    miles   = 1000.0       # A floating point
    name    = "John"       # A string

    print counter   //100
    print miles     //1000.0
    print name      //John

赋值-多次版
~~~~~~~~~~~~~~~~~~~~~~
Python允许您同时为多个变量分配单个值。例如 -
:: 
    # 这里，使用值1创建整数对象，并将所有三个变量分配给相同的内存位置。
    a = b = c = 1
    # 这里，两个值为1和2的整数对象分别分配给变量a和b，一个值为“john”的字符串对象分配给变量c。
    a,b,c = 1,2,"john"

赋值-机构版 （3.x）[in prcess]
~~~~~~~~~~~~~~

:: 

    mode = (2,3,4,5,6) //如果这里的元素不等于被赋值的变量数量，则报错
    a,b,c,d,e = mode
    print a     # 2
    print b     # 3
    print c     # 4
    print d     # 5
    print e     # 6

标准数据类型
~~~~~~~~~~~~~~~
存储在存储器中的数据可以是多种类型。例如，一个人的年龄被存储为数字值，他或她的地址被存储为字母数字字符。Python有各种标准数据类型，用于定义可能的操作以及每种操作的存储方法。

Python有五种标准数据类型 -

    * integer
    * string
    * List
    * Tuple
    * Dictionary

数字类型
~~~~~~~~~~~~~
    * int (signed integers)
    * long (long integers, they can also be represented in octal and hexadecimal)
    * float (floating point real values)
    * complex (complex numbers)

===     =====           =====   ========
int	    long	        float	complex
===     ======          ======  ========
10      51924361L   	0.0     3.14j
100 	-0x19323L	    15.20   45.j
-786	0122L           -21.9	9.322e-36j
080     0xDEFABCECBDAECBFBAEl	32.3+e18	.876j
-0490	535633629843L   -90.	-.6545+0J
-0x260	-052318172735L	-32.54e100	3e+26J
0x69	-4721885298529L	70.2-E12	4.53e-7j
=====   ======          =====       ======


Python字符串
~~~~~~~~~~~~~~
Python中的字符串被标识为引号中表示的连续字符集。Python允许使用单引号或双引号。可以使用切片运算符（[]和[：]）获取字符串子集，索引从字符串开头的0开始，并从最后的-1开始。加号（+）是字符串连接运算符，星号（*）是重复运算符。例如 -

:: 
    #!/usr/bin/python

    str = 'Hello World!'

    print str          # Prints complete string
    print str[0]       # Prints first character of the string
    print str[2:5]     # Prints characters starting from 3rd to 5th
    print str[2:]      # Prints string starting from 3rd character
    print str * 2      # Prints string two times
    print str + "TEST" # Prints concatenated string

    # 输出结果如下
    Hello World!
    H
    llo
    llo World!
    Hello World!Hello World!
    Hello World!TEST

list
~~~~~~~~~
list是Python中最通用的复合数据类型。list包含以逗号分隔的项目，并用方括号（[]）括起来。在某种程度上，list类似于C中的数组。它们之间的一个区别是属于list的所有项目可以是不同的数据类型。
存储在list中的值可以使用切片运算符（[]和[：]）进行访问，索引从list开头的0开始，然后一直运行到结束-1。加号（+）是list连接运算符，星号（*）是重复运算符。例如 -

:: 
    #!/usr/bin/python

    list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
    tinylist = [123, 'john']

    print list          # Prints complete list
    print list[0]       # Prints first element of the list
    print list[1:3]     # Prints elements starting from 2nd till 3rd 
    print list[2:]      # Prints elements starting from 3rd element
    print tinylist * 2  # Prints list two times
    print list + tinylist # Prints concatenated lists

    # 输出
    ['abcd', 786, 2.23, 'john', 70.2]
    abcd
    [786, 2.23]
    [2.23, 'john', 70.2]
    [123, 'john', 123, 'john']
    ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']

Tuple
~~~~~~~~
 Tuple 是另一种类似于列表的序列数据类型。 Tuple 由逗号分隔的许多值组成。但是，与列表不同， Tuple 括在括号内。
列表和 Tuple 之间的主要区别是：列表括在括号（[]）中，它们的元素和大小可以更改，而 Tuple 括在括号（（）中）并且无法更新。 Tuple 可以被认为是只读列表。例如 -
:: 
    #!/usr/bin/python

    tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
    tinytuple = (123, 'john')

    print tuple           # Prints complete list
    print tuple[0]        # Prints first element of the list
    print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
    print tuple[2:]       # Prints elements starting from 3rd element
    print tinytuple * 2   # Prints list two times
    print tuple + tinytuple # Prints concatenated lists
    # 运行后得到以下的结果
    ('abcd', 786, 2.23, 'john', 70.2)
    abcd
    (786, 2.23)
    (2.23, 'john', 70.2)
    (123, 'john', 123, 'john')
    ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')

direction

    Python的direction是一种哈希表类型。它们像在Perl中找到的关联数组或散列一样工作，并由键值对组成。direction键几乎可以是任何Python类型，但通常是数字或字符串。另一方面，值可以是任意Python对象。direction用大括号（{}）括起来，可以使用方括号（[]）分配和访问值。例如 -
    
:: 

    #!/usr/bin/python

    dict = {}
    dict['one'] = "This is one"
    dict[2]     = "This is two"

    tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


    print dict['one']       # Prints value for 'one' key
    print dict[2]           # Prints value for 2 key
    print tinydict          # Prints complete dictionary
    print tinydict.keys()   # Prints all the keys
    print tinydict.values() # Prints all the values

    # 运行结果
    This is one
    This is two
    {'dept': 'sales', 'code': 6734, 'name': 'john'}
    ['dept', 'code', 'name']
    ['sales', 6734, 'john']

类型之间转换
==============
【todo】