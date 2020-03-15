#!/usr/bin/python3
import shutil
import psutil
import os




def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    global free
    free = du.free / du.total * 100
    txt = 'Free disk space is {}'
    print(txt.format(free))
    return free > 20

def check_cpu_usage():
    global usage
    usage = psutil.cpu_percent(1)
    txt = 'CPU usage is {}%'
    print(txt.format(usage))
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is ok!")
