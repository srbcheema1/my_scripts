import sys
import time
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        sys.stdout.write("%s \r" % i)
        time.sleep(0.1)
        sys.stdout.flush()
