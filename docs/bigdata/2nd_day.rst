install VirtualBox && Hadoop && Hive 
========================================

本次重点
------------
    1. VirtualBox -- 安装
    2. Hadoop -- 安装并配置JDK软件环境
    3. Hive 框架
    4. Hive 安装
    5. 运行 Hive 和 执行 query


概念回顾
-----------
    NameNode: 名字端对不存储数据（文件）本身，而是存储数据（文件）的索引（index），帮助用户快速获取数据端（DataNode）的数据Blocks。

    TODO:理解block storage

Hadoop 安装
--------------------



.. code::
    // 
    > yum update

    // step 1 配置Hadoop的运行环境

    > hostnamectl set-hostname master
    > vim /etc/hosts
    // 获取VM的IP地址
    > ifconfig
    // 下载Java 的JDK
    > curl -LO -H "Cookie:oraclelicense=accept-securebackup-cookie" https://edelivery.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.rpm
    > rpm -Uvh jdk-8u181-linux-x64.rpm


    // step 2 配置 Hadoop 用户
    
    > useradd -d /opt/hadoop hadoop
    > passwd hadoop 

    // step 3 下载 Hadoop 软件
    > curl -O http://mirrors.hust.edu.cn/apache/hadoop/common/hadoop-2.8.5/hadoop-2.8.5.tar.gz
    > tar -xfz hadoop-2.8.5.tar.gz
    > cp -rf hadoop-2.8.3/* /opt/hadoop/
    > chown -R hadoop:hadoop /opt/hadoop/

/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.181-3.b13.el7_5.x86_64/jre/
    // step 4 编辑.bash_profile的环境变量
    > update-alternatives --config java
    java-1.8.0-openjdk.x86_64 (/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.181-3.b13.el7_5.x86_64/jre/bin/java)
    java-1.7.0-openjdk.x86_64 (/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.191-2.6.15.4.el7_5.x86_64/jre/bin/java)
    // 修改.bashrc
    #HADOOP VARIABLES START
    export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.191-2.6.15.4.el7_5.x86_64/jre
    export HADOOP_INSTALL=/home/hadoop/opt/hadoop
    export PATH=$PATH:$HADOOP_INSTALL/bin
    export PATH=$PATH:$HADOOP_INSTALL/sbin
    export HADOOP_MAPRED_HOME=
    > su -hadoop
    > cd /home/[username] | vi .bash_profile
    在vi编辑器中追加
        ## java env variables
        export PATH=$PATH:$JAVA_HOME/bin
        export CLASSPATH=$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar
        ## Hadoop env variables
        export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.191-2.6.15.4.el7_5.x86_64/jre
        export HADOOP_HOME=/home/hadoop/opt/hadoop
        export HADOOP_COMMON_HOME=$HADOOP_HOME
        export HADOOP_HDFS_HOME=$HADOOP_HOME
        export HADOOP_MAPRED_HOME=$HADOOP_HOME
        export HADOOP_YARN_HOME=$HADOOP_HOME
        export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/"
        export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
        export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
        


    // step 5 初始化环境变量
    > source .bash_profile
    > echo $HADOOP_HOME
    > echO $JAVA_HOME

    // step 6 设置ssh
    > ssh-keygen -t rsa
    > ssh-copy-id master.hadoop.lan

    // step 7 设置Hadoop 配置文件
    > vi etc/hadoop/core-site.xml
<property>
    <name>fs.defaultFS</name>
    <value>hdfs://master.Hadoop.lan:9000/</value>
</property>

    // step 8 编辑hdfs-site.xml 文件
    > vi etc/hadoop/hdfs-site.xml
<property>
    <name>dfs.data.dir</name>
    <value>file:///opt/volume/datanode</value>
</property>
<property>
    <name>dfs.name.dir</name>
    <value>file:///opt/volume/namenode</value>
</property>

    //如果指定的文件夹 datanode和namenode 没有需要创建一下，他不会自动
    su root
    mkdir -p /opt/volume/namenode
    mkdir -p /opt/volume/datanode
    chown -R hadoop:hadoop /opt/volume/
    ls -al /opt/ #verify permissions
    exit

    // step 9 创建mapred-site.xml
    > vi etc/hadoop/mapred-site.xml
<configuration>
<property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
</property>
</configuration>

    // step 10 配置yarn-site.xml
    >vi etc/hadoop/yarn-site.xml
<property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
</property>

    // 设置 hadoop-env.ssh
    > vi etc/hadoop/hadoop-env.sh
    export JAVA_HOME=/usr/java/default/
    
    > vi etc/hadoop/slaves

    // step 11 格式化Hadoop
    //hadoop中的格式化主要是对namenode 来说的，本质上来说是格式化 */opt/volume/namenode*
    > hdfs namenode -format


    截止到目前已经安装完毕
    
    TODO: 第二段05:20

hadoop 的简单使用
-------------------

.. code::

    > hdfs dfs -mkdir /my_storage
    > hdfs dfs -put /my_storage/[filename]

    > hdfs dfs -cat /my_storage/[filename]
    > hdfs dfs -ls /my_storage/

    > hdfs dfs -get /my_storage/ ./
    > hdfs dfs -help


hadoop 在浏览器中查看
---------------------------

http://[ip|hostname]:50070/

Hadoop 服务 启动和停止
---------------------------

    > hadoop/sbin/start-yarn.sh
    > hadoop/sbin/start-dfs.sh
    > hadoop/sbin/stop-yarn.sh
    > hadoop/sbin/stop-dfs.sh

    > su -root # vi /etc/rc.local
    su -hadoop -c "/opt/hadoop/sbin/start-dfs.sh"
    su -hadoop -c "/opt/hadoop/sbin/start-yarn.sh"


    
作业
-------
按照hadoop的部署流程过一遍