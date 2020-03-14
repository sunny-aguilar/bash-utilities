#!/usr/bin/python3
import shutil
import psutil

txt1 = 'Free disk space is {}'
txt2 = 'CPU usage is {}'
free = 0
usage = 0

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    txt1 = "Free disk space is {}".format(free)
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    txt2 = "CPU usage is {}".format(usage)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage:
    print("ERROR!")
else:
    print("Everything is ok!")
    print(txt1)
    print(txt2)
