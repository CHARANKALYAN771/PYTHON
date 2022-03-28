from datetime import date
from time import time

dat=date.max
dat1=date.min
print(dat)
print(dat1)
dat=date(2020,10,20)

print("year:",dat.year)
print("month:",dat.month)
print(time.ctime())
x=date.today()
print(x)
y=x.isocalendar()
z=list(y)
print(y)

print(date.fromisoformat('2020-12-20'))
x=1234567
dat=date.fromordinal(x)
print("%d is :%s"%(x,dat));

today =time()
print(today)
dat= date.fromtimestamp(today)
print("date is : %s "%dat)

today =date.fromtimestamp(time())
dat=today.isoformat()
print("%s"%dat)


import datetime 
res = datetime.datetime.now()  
print(res)
from datetime import date
res = date.today()
cd=res.strftime("%B")
print(cd)
