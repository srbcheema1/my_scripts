import time
import sys
from tkinter import messagebox

if (len(sys.argv)>1):
	max_time = int(sys.argv[1])
else :
	max_time = 15

minutes = max_time
sys.stdout.write("\n\t--------------\n\t    TIMER\n\t--------------\n")
while minutes >= 0:
	sys.stdout.write("\tT - %s minutes   \r" % (minutes))
	time.sleep(60)
	sys.stdout.flush()   
	minutes -= 1

messagebox.showinfo("Timer", "Timer ended")
