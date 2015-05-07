__author__ = 'rohan'
import os
from os import path
p = '/home/rohan/Downloads/resultszip_FILES/results'
files = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
# print files
speed = {}
for f in sorted(files):
    if "speedtest" in f:
        day = f.split('_')[0].replace("run","")
        fd = open(p+"/"+f)
        lines = fd.readlines()
        for line in lines:
            if "Download:" in line:
                print line.split(' ')[1]
                speed[day]=line.split(' ')[1]

print speed
