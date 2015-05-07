__author__ = 'rohan'
import os
p = '/home/rohan/Downloads/resultszip_FILES/results'
i = 0
data = {}
# data["time_download"] = []
# data["time_comp"] = []
# data["download_dns"] = []
# print sorted(os.listdir(p))
# list = sorted(os.listdir(p))
# print type(list[1])

sorted_dir = []
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
                # print line.split(' ')[1]
                speed[day]=line.split(' ')[1]

print speed
# for root,dirs,files in os.walk(p):
    # print root1
    # for root1,dirs1,files1 in os.walk(root):
    #     if i==0:
    #         print "nothing"
    #     else:
    # print dirs
    # sorted_dir = sorted(dirs)
sorted_dir = [ name for name in os.listdir(p) if os.path.isdir(os.path.join(p, name)) ]
sorted_dir = sorted(sorted_dir)
# print(sorted_dir)
# print len(sorted_dir)
for i in range(len(sorted_dir)):
    root = p+"/"+sorted_dir[i]
    # print speed[sorted_dir[i]]
    # print sorted_dir
    # print root
    cur_speed = float(speed[sorted_dir[i]])
    for file in os.listdir(root):
        # print root+"/"+file
        f = open(root+"/"+file)
        lines =  f.readlines()
        # print file,lines
        temp = []
        try:
            for line in lines:
                if "time_download:" in line:
                    temp.append(100/(float(line.split(':')[1].strip())/cur_speed))
                    # data["time_download"].append(line.split(':')[1].strip())
                    # data["time_download"]= line.split(':')[1].strip()
                    # print line.split(':')[1].strip()
                if "time_comp:" in line:
                    temp.append(100/(float(line.split(':')[1].strip())/cur_speed))
                    #data["time_comp"].append(line.split(':')[1].strip())
                    # data["time_comp"]= line.split(':')[1].strip()
                    # print line
                if "download_dns:" in line:
                    temp.append(100/(float(line.split(':')[1].strip())/cur_speed))
                    # data["download_dns"].append(line.split(':')[1].strip())
                    # data["download_dns"]= line.split(':')[1].strip()
                    # print line
            # print temp
            # print file
        except ZeroDivisionError:
            pass
        if file not in data.keys():
            data[str(file)] = [temp]
        else:
            data[str(file)].append(temp)
    #     # print root1
# i+=1
print data
data_len = len(data)
c = 0
target = []
for k in data:
    if len(data[k])>5:
        c+=1
        target.append(k)
print c
print(target)

final = []
for i in range(len(target)):
    site = target[i]
    for k in data:
        # print data[k]
        if k==site:
            num = len(data[k])
            if num>5:
                temp = []
                try:
                    for j in range(num):
                        temp.append(data[k][j][2])    #0 is index for download time, change this for others
                except IndexError:
                    pass
                final.append(temp)
#print(final)

print(len(final))
for i in range(len(final)):
    print(target[i])
    for j in range(len(final[i])):
        print final[i][j]






# #format of data
# #{"url":[[time_download,time_comp,download_dns],[time_download,time_comp,download_dns],[]...],
# #"url":[[time_download,time_comp,download_dns],[time_download,time_comp,download_dns],[]...]....}