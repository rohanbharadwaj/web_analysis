__author__ = 'rohan'
f = open("dat.txt")
lines = f.readlines()
data = {}
for line in lines:
    if "time_download:" in line:
        data["time_download"]= line.split(':')[1].strip()
        print line.split(':')[1].strip()
    if "time_comp:" in line:
        data["time_comp"]= line.split(':')[1].strip()
        print line
    if "download_dns:" in line:
        data["download_dns"]= line.split(':')[1].strip()
        print line

print(data)