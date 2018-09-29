Apache Hadoop && Hive && Spark
=================================

Enterprise Data Trends (企业数据趋势)
----------------------------------------

Sentiment(有倾向的看法)
    简单的讲就是依据数据来源，分析语言所表达的主观意愿信息。通过信息获取进行意愿追踪，并识别影响者。

Clickstream(个人浏览记录)
    通过记录用户浏览网页记录留下的浏览路径等线索。分析路径，优化网站设计。

Geographic(具有地理特性的)
    通过获取用户的物理地址数据。这样的数据广泛应用于物流业，租赁（汽车，电动车），安全产品。允许组织优化路线，预测库存水平。
server log
    主要是服务器运行过程中产生的服务器运行日志。
Text(SNS的观点)
    通过网络媒体中的文字评论，获取的人们的想法观点。通过对这些数据的收集，分析，可以帮助决策者预测未来的流行趋势，社会发展走向等。

Causation to correlation (诱因关联)
    大数据可以允许组织，从更加详细的数据中获取更准确的结果。另外，大数据能够提前获取预测业务和业务延时之间，成为一个组织成功可能与否十分关键的因素。


什么是Hadoop？
---------------
Hadoop出现的背景
    - 大数据存储要求
    - 容灾容错
    - 成本
    - 版权问题

hadoop 1.0
    HDFS : Hadoop File System
        1. 重复存储
        2. index
    MapReduce : 
        1. 是一个范式

hadoop 2.0 
    1. Hadoop Common 为其他Hadoop模块提供支持
    2. HDFS Hadoop分布式文件系统
    3. MapReduce 可伸缩和并行处理大量数据集
    4. Yarn 一个负责作业调度和聚合资源管理

Hive:
    使用结构化语言进行读取的HDFS数据的应用软件，就像使用数据库一样

Hadoop cluter
    1. NameNode 管理HDFS命名的服务器,存储索引
    2. DataNode 承担数据Store功能的服务器，存储大文件
    3. NodeManager 
    4. ResourceManager 

EDW ： Enterprise Data Warehouse。


what is a File System?
    - OS architecture
    - HDFS Architecture
    - Understanding Block Storage
    - Demonstration: Block Storage
    - The NameNode
    - The DataNodes
    - DataNode Failure
    - HDFS Clients

