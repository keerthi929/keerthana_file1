#to import threading 

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")


#output

Starting Thread-1
Starting Thread-2
Thread-1: Tue Jul 13 18:57:49 2021
Thread-2: Tue Jul 13 18:57:50 2021
Thread-1: Tue Jul 13 18:57:50 2021
Thread-1: Tue Jul 13 18:57:51 2021
Thread-2: Tue Jul 13 18:57:52 2021
Thread-1: Tue Jul 13 18:57:52 2021
Thread-1: Tue Jul 13 18:57:53 2021
Exiting Thread-1
Thread-2: Tue Jul 13 18:57:54 2021
Thread-2: Tue Jul 13 18:57:56 2021
Thread-2: Tue Jul 13 18:57:58 2021
Exiting Thread-2
Exiting Main Thread

[Program finished]