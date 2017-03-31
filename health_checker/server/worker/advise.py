#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals


class Advise(object):
    binlog_format_warning="您的配置参数binlog_format设置为{0}，建议设置为{1}，否则有主、从数据不一致的风险"
    sync_binlog_warning="您的配置参数sync_binlog设置为{0}，建议设置为{1}，否则有主、从数据不一致的风险"
    expire_binlog_days_warning="您的配置参数expire_logs_days设置为{0}，建议设置为{1}，否则存在binlog占用太多磁盘空间的风险"
    binlog_size_too_large="您的磁盘空间为{0}，您的binlog占用空间为{1}，超过了阈值{2}%，建议您适当调小expire_logs_days，减少二进制日志保留时间"

    innodb_flush_log_at_trx_commit="您的数据库配置参数innodb_flush_log_at_trx_commit取值为{0}，建议您修改该值为{1}，否则当数据库宕机时，您的数据存在丢失风险"
    innodb_flush_method="您的数据库配置参数innodb_flush_method取值为{0}，建议您修改该值为{1}，否则当操作系统宕机时，您的数据存在丢失风险"
    innodb_log_file_size="您的磁盘空间为{0}，您的数据库配置参数innodb_log_file_size取值为{1}，该值太大会影响数据库故障恢复的速度，该值太小会影响数据库的性能，根据您的磁盘空间，我们建议您取值为{2}到{3}之间"

    max_connection_warning="数据库连接数过多容易造成线程频繁的上下文切换，连接数过少不能充分发挥数据库的性能，您的数据库连接数是{0}，你的buffer pool大小是{1}，建议您的数据库连接数设置在{2}~{3}范围内，也可以直接设置为{4}"


    slave_io_running_error="您的从机IO线程没有运行，请立刻手动修复该线程"
    slave_sql_running_error="您的从机SQL线程没有运行，请立刻手动修复该线程"
    last_io_error="您的从机复制出错，详情请查看Last_IO_Error信息，请立即手动修复该错误"
    last_sql_error="您的从机复制出错，详情请查看Last_SQL_Error信息，请立即手动修复该错误"
    relay_log_recovery="您的从机配置参数relay_log_recovery设置为{0}，从机宕机后存在主从数据不一致的风险，请修改该参数为{1}"
    relay_log_info_repository="您的从机配置参数relay_log_info_repository设置为{0}，从机宕机后存在主从数据不一致的风险，请修改该参数为{1}"


# # 索引检查优化建议
# NoPrimaryKey=您的数据库{0}下的表{1}缺乏主键，建议添加主键
# RedundancyPrefixIndex=根据索引最左前缀匹配原则，您的数据库{0}下的表{1}中{2}索引是多余的，因为您已经创建了{3}索引
#
# RedundancyEndsWithPrefixIndex=您的数据库{0}下的表{1}中，索引{2}的后缀是聚集索引{3}的前缀，您可以考虑将索引{2}中的{4}字段去除
# IndexCardinalityTooLow=您的数据库{0}下的表{1}索引列区分度低于{2}，您可以考虑删除该索引。索引名：{3}，列区分度：{4}%
# InvalidIndex=您的数据库{0}下的表{1}存在{2}天未被使用过的索引，您可以考虑删除该索引列。索引名：{3}
#
# SlaveThreadNotRuning=您的从机复制线程SLave Thread已经中断，请立刻手动修复复制线程
#



# BufferPoolTooLargeWarning=您的系统可用内存为{0}，建议您的配置参数innodb_buffer_pool_size小于等于{1}
# BufferTooLargeInTheory=您的系统可用内存为{0}，您的配置参数max_connections为{1}，理论上您的数据库最大占用内存为{2}，建议调整Innodb_buffer_pool_size, max_connections参数或者升级规格
#
# # 容量规划优化建议
# CpuUsageRateTooHigh=您的数据库CPU利用率在{0}至{1}这段时间内，超过{2}%的时间CPU利用率高于{3}%，建议您升级规格
# IoUtilRateTooHigh=您的数据库磁盘IO利用率在{0}至{1}这段时间内，超过{2}%的时间磁盘IO利用率高于{3}%，建议您扩大磁盘空间
# MemoryUtilTooLow=在{0}至{1}这段时间内，您的数据库内存命中率有超过{2}%的时间低于{3}%，建议您升级规格
# NetworkBindWidthTooHigh=在{0}至{1}这段时间内，您的数据库公网带宽利用率有超过{2}%的时间高于{3}%，建议您调大网络带宽
# ReminderStorageTooLow=您的数据库当前的剩余磁盘空间少于{0}，建议您扩大磁盘空间
# StorageWillFull=在未来7天内，您的数据库磁盘空间可能被用完，建议您扩大磁盘空间
#


# ReplicationPerformanceTooPoor=您的从机复制延迟在{0}~{1}这段时间内，有超过{2}%的复制时间大于{3}秒，建议您尝试从以下几个角度优化从机数据库性能：检查网络性能，提高实例规格配置，开启并行复制等
# SlowLogTooMany=您的数据库慢日志在{0}~{1}这段时间内，有超过{2}%的时间，每秒的慢日志数超过{3}条，请及时优化SQL语句或者升级规格

# AutoHealthCheck=您的数据库未开启自动定时体检，请在设置页面开启，及早预知系统风险，将风险消灭在摇篮中
# CheckPrivileges=您的公网数据库账户{0}授权访问的IP范围过大，存在安全隐患，请及时修改
# CheckNetworkSecurity=您的公网数据库容器没有设置任何IP限制规则，存在安全隐患，建议添加iptables规则，限制IP访问
# WeakPasswordChar=您的数据库账户{0}密码长度小于等于3，风险等级较高，请及时修改密码
# WeakPasswordDigit=您的数据库账户{0}密码小于等于5个纯数字，风险等级较高，请及时修改密码
# WeakPasswordCommon=您的数据库账号{0}的密码使用频率过高，存在安全隐患，请及时修改密码
# MySQLDeadLockWarning=您的数据库在过去{0}小时内，发生了{1}次死锁，死锁频率较高，可能影响数据库性能，您可以查看Error log找到死锁语句，请重新审核SQL语句，合理组织SQL语句的顺序