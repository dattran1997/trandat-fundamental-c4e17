from datetime import *

now = datetime.now()
#print (now.day,now.month,now.year,now.hour,now.minute,now.second)
print ("{0}/{1}/{2}, {3}:{4}:{5}".format(now.day,now.month,now.year,now.hour,now.minute,now.second))
