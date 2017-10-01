#!/usr/bin/env python3

import os
from os.path import basename
import pyinotify

dirname = "/home/redrield/Documents/Classroom" # Change directory to what you want here
rcloneDriveName = "School Drive" # Change rclone drive to the one you've defined and you want to sync

watchManager = pyinotify.WatchManager()

mask = pyinotify.IN_DELETE | pyinotify.IN_MODIFY | pyinotify.IN_CREATE

watchManager.add_watch(dirname, rec=True, mask=mask)


def handler(ev):
    os.system("""rclone sync {} "{}:/{}" """.format(dirname, rcloneDriveName, basename(dirname)))


notifier = pyinotify.Notifier(watchManager, handler)
notifier.loop()
