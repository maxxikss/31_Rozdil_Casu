from datetime import datetime

date=datetime.strptime('2022-01-11 11:28:41,035','%Y-%m-%d %H:%M:%S,%f')

now=datetime.now()
diff=now-date
print(diff)