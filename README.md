# rds_manager
阿里云rds自动备份和备份文件启动


## 配置说明
在config.py中设置
<!--lang:python-->
    ACCESSKEYID = ''
    ACCESSKEYSECRET = ''
在getDBbackupurl.py中设置
<!--lang:python-->
    DBInstanceID=''
文件备份路径为/data/rdsbackup/ 
## 定时自动获取备份
通过阿里云提供的rds api，下载阿里云rds一天内物理备份的文件
可以配置如下crontab来实现自动下载

<!--lang:bash-->
    git clone git@github.com:francisar/rds_manager.git
    crontab -e
    * 5 * * * * cd [project path] && ./getDBback.sh > /dev/null 2>&1


## 将备份启动
项目shell目录下的rdsbackupstart，可以通过docker将下载的物理备份文件启动成mysql实例
不过需要先将shell路径下的rds_backup_extract加入PATH，并且安装
[Percona-XtraBackup](http://www.percona.com/downloads/XtraBackup/ 'Percona-XtraBackup')
<!--lang:bash-->
    cd /data/rdsbackup/
    rdsbackupstart  hins.tar.gz 33060 rds7h9


即可通过33060端口访问数据库（没有权限验证），初次启动，因为需要去dockerhub下载docker镜像，所以会比较慢