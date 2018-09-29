安装执行环境
===============

能运行在什么OS上？
~~~~~~~~~~~~~~~~~~~

    * Unix (Solaris, Linux, FreeBSD, AIX, HP/UX, SunOS, IRIX, etc.)
    * Windows
    * Macintosh (Intel, PPC, 68K)
    * OS/2
    * DOS (multiple versions)
    * PalmOS
    * Nokia mobile phones
    * Acorn/RISC OS
    * BeOS
    * Amiga
    * VMS/OpenVMS
    * QNX
    * VxWorks
    * Psion
    * Python 可以移植到 Java and .NET VM(virtual machines)

.. note::笔者承认Python的适用性和笔者的眼界形成了鲜明的对比，但是笔者也知道通过在Command Line键入python可以检查版本号

官网资源
~~~~~~~~
最新和最新的源代码，二进制文件，文档，新闻等，可在Python官方网站 ..https://www.python.org/ : https://www.python.org/ 上找到。
您可以从 ..https://www.python.org/doc/: https://www.python.org/doc/ 下载Python文档。该文档以HTML，PDF和PostScript格式提供。

安装
~~~~~~

Unix / Linux
--------------
以下是在Unix / Linux机器上安装Python的简单步骤。

    1. 打开Web浏览器并转到 https://www.python.org/downloads/ 。

    2. 点击链接下载适用于Unix / Linux的压缩源代码。

    3. 下载并解压缩文件。tar -zxvf [tar文件]

    4. 如果要自定义某些选项，请编辑模块/设置文件。

    5. 运行./configure脚本

    6. make

    7. make install

安装完成后设置

    * 在csh shell中 - 键入setenv PATH“$ PATH：/usr/local/bin/python”并按Enter键。

    * 在bash shell（Linux）中 - 键入export PATH =“$PATH:/usr/local/bin/python”并按Enter键。

    * 在sh或ksh shell中 - 键入PATH =“$ PATH:/usr/local/bin/python”并按Enter键。

注 - /usr/local/bin/python是Python目录的路径

windows
----------

    找到windows 的安装包，下载按照步骤安装。安装完成后修改环境变量
    在命令提示符下 - 键入path％path％; C：\ Python并按Enter键。
    注 - C：\ Python是Python目录的路径

Macintosh
----------

苹果操作系统中自带一个python2.7版本、

运行Python
~~~~~~~~~~~~

首先在命令行，键入 
$python # Unix/Linux
or
python% # Unix/Linux
or
C:> python  # Windows/DOS