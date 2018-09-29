基本语法
==========

Python 作为一门编程语言它和很多其他的语言有很多类似的特型，诸如Perl，C和Java。但是也有其独特的语法特征。本节作为入门课程重点聊聊其特征的语法。

体验交互式编程
~~~~~~~~~~~~~~~

:: 
    
    python //安装2.x版本
    or
    python3 //安装3.x版本

    >>> print("hello, Python")
    hello，Python


脚本模式编程
~~~~~~~~~~~~~~

我们用另一种方法实现和上面一样的例子，我们假设目前所在的路径是path，并且打开了一个终端。

    1. 将下面这段话写入到一个test.py文件中
        #!/usr/bin/python
        print "Hello, Python!"
    2.  在终端中执行 python test.py 或者 python3 test.py

Python 的命名规则
~~~~~~~~~~~~~~~~~~~~

以下是Python标识符的命名约定 -

    * 类名以大写字母开头。所有其他标识符以小写字母开头。

    * 使用单个前导下划线启动标识符表示标识符是私有的。

    * 启动带有两个前导下划线的标识符表示强私有标识符。

    * 如果标识符也以两个尾部下划线结尾，则标识符是语言定义的特殊名称。

保留字
~~~~~~
        and	exec	not
        assert	finally	or
        break	for	pass
        class	from	print
        continue	global	raise
        def	if	return
        del	import	try
        elif	in	while
        else	is	with
        except	lambda	yield

运行流控制
~~~~~~~~~~~~~~~~
Python没有提供大括号来指示类和函数定义或流控制的代码块。代码块由行**缩进**表示，这是严格执行的。
缩进中的空格数是可变的，但块内的所有语句**必须缩进相同的数量**。例如
:: 

    if True:
        print "True"
    else:
        print "False"

多行语句
~~~~~~~~

Python中的语句通常以新行结束。但是，Python确实允许使用行继续符（\）来表示该行应该继续。例如 -

:: 

    total = item_one + \
            item_two + \
            item_three

[]，{}或（）括号中包含的语句不需要使用行继续符。例如 -
:: 

    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday']


Python 的string
~~~~~~~~~~~~~~~~~~~~
Python接受单引号（'），双引号（“）和三引号（'''或”“”）来表示字符串文字，只要相同类型的引号开始和结束字符串即可，三引号用于跨越多行跨越字符串。例如，以下所有内容都是合法的 -
:: 

    word = 'word'
    sentence = "This is a sentence."
    paragraph = """This is a paragraph. It is
    made up of multiple lines and sentences."""

Python 中的注释
    不在字符串文字内的井号（＃）开始注释。＃之后的所有字符和直到物理行的末尾都是注释的一部分，Python解释器忽略它们。

:: 

    #!/usr/bin/python

    # First comment
    print "Hello, Python!" # second comment

用户输入
~~~~~~~~~~~~

:: 

    #!/usr/bin/python

    raw_input("\n\nPress the enter key to exit.")

一行里的多个语句
~~~~~~~~~~~~~~~~~~~~

分号（;）允许单行上的多个语句，因为两个语句都不会启动新的代码块。这是使用分号的示例片段 -

:: 

    import sys; x = 'foo'; sys.stdout.write(x + '\n')

多个语句作为
~~~~~~~~~~~~~~~~
一组单独的语句，它们构成一个代码块，在Python 中称为套件。复合或复杂语句（例如if，while，def和class）需要标题行和套件。标题行开始语句（使用关键字）并以冒号（:)结束，后跟一行或多行组成套件。例如 -
:: 

    if expression : 
        suite
    elif expression : 
        suite 
    else : 
        suite