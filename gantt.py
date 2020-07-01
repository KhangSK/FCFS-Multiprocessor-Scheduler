import sys
import matplotlib.pyplot as plt 
from cv2 import cv2
from PIL import Image
  
# Declaring a figure "gnt" 
fig, gnt = plt.subplots() 

# Setting labels for x-axis and y-axis 
gnt.set_xlabel('Gantt Chart') 
gnt.set_ylabel('Processor') 

f = open('input.txt', 'r')
numProcessor = int(f.readline())

arrPosition = []
arrCPU = []
temp = 10
exe = {}
for i in range(numProcessor):
    arrPosition += [temp]
    temp += 10 
    arrCPU += [('CPU ' + str(i + 1))]
    exe[('CPU ' + str(i + 1))] = 0
numProcesses = int(f.readline())
A = {}
B = {}
minArri = float("inf")
maxArri = float("-inf")
for i in range(numProcesses):
    line = f.readline()
    parts = line.split(';')
    A[parts[0]] = int(parts[1])
    B[parts[0]] = int(parts[2])
    if minArri > A[parts[0]]: minArri = A[parts[0]]
    if maxArri < A[parts[0]]: maxArri = A[parts[0]]
# Setting Y-axis and X-axis limits 

gnt.set_ylim(0, temp) 

# Setting ticks on y-axis 
gnt.set_yticks(arrPosition) 
# Labelling tickes of y-axis 
gnt.set_yticklabels(arrCPU) 
# Setting graph attribute 
gnt.grid(True)


colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
count = 0

for i in range(minArri, maxArri + 1):
    for j in A:
        if A[j] == i:
            execute = False
            for k in range(len(exe)):
                if exe['CPU ' + str(k + 1)] == A[j]:
                    execute = True
                    gnt.broken_barh([(exe['CPU ' + str(k + 1)], B[j])], (8 + k * 10, 4), color = colors[count])
                    gnt.annotate('Process ' + j, (exe['CPU ' + str(k + 1)] , 10 + 10 * k))
                    exe['CPU ' + str(k + 1)] += B[j]
                    count += 1
                    break
            if not execute:
                temp = float("inf")
                index = ""
                pos = -1
                for k in range(len(exe)):
                    if temp > exe['CPU ' + str(k + 1)]:
                        temp = exe['CPU ' + str(k + 1)]
                        index = 'CPU ' + str(k + 1)
                        pos = k
                if A[j] > exe[index]:
                    exe[index] = A[j] + B[j]
                    gnt.broken_barh([(A[j], B[j])], (8 + pos * 10, 4), color = colors[count])
                    gnt.annotate('Process ' + j, (A[j] , 10 + 10 * pos))
                else:
                    gnt.broken_barh([(exe[index], B[j])], (8 + pos * 10, 4), color = colors[count]) 
                    gnt.annotate('Process ' + j, (exe[index] , 10 + 10 * pos))         
                    exe[index] += B[j]
                count += 1
maxExe = float("-inf")
for i in exe:
    if maxExe < exe[i]: maxExe = exe[i]
gnt.set_xlim(0, maxExe + 1)

  
plt.savefig("gantt1.png") 
f = Image.open("gantt1.png").show()

