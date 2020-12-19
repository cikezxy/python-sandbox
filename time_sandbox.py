import time

# wall clock time
print('The time is:', time.time())
print(time.localtime())
print(time.mktime(time.localtime()))

print('The time is      :', time.ctime())
later = time.time() + 15
print('15 secs from now :', time.ctime(later))
print(time.asctime())


