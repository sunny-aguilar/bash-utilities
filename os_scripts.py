#!/usr/bin/python3
import shutil
import psutil

txt1 = 'Free disk space is {}'
txt2 = 'CPU usage is {}'
# free = 0
# usage = 0

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    global free
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    global usage
    usage = psutil.cpu_percent(1)
    print(usage)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage:
    print("ERROR!")
else:
    print("Everything is ok!")
    print(txt1.format(free))
    print(txt2.format(usage))
