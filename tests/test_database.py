__author__ = 'hzlaimingxing'


from health_checker.client.database.mysql import DatabaseManager



d = dict(host="59.111.124.115", user='laimingxing', password='laimingxing', size=3)
db = DatabaseManager(**d)
print(db.binlog_size)


