import sys
import matplotlib.pyplot as plt
from cv2 import cv2
from PIL import Image

def draw_gantt(CPUs, time, proclist):
    """ Draw gantt chart based on CPUs history and time elapsed"""
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()

    # Setting labels for x-axis and y-axis 
    gnt.set_xlabel('Gantt Chart')
    gnt.set_ylabel('Processor')

    arrPosition = []
    arrCPU = []
    y_tick_range = 10
    for i in range(len(CPUs)):
        arrPosition += [y_tick_range]
        y_tick_range += 10
        arrCPU.append(CPUs[i].cpuname)

    # Setting Y-axis and X-axis limits
    gnt.set_ylim(0, y_tick_range)
    gnt.set_xlim(0, time + 1)
    # Setting ticks on y-axis 
    gnt.set_yticks(arrPosition) 
    # Labelling tickes of y-axis 
    gnt.set_yticklabels(arrCPU)
    # Setting graph attribute 
    gnt.grid(True)

    for i in 
    print(len(proclist))

    for x in range(time):
        for y in range(len(CPUs)):
            if CPUs[y].history[x] is not None:
                color = CPUs[y].history[x]
                gnt.broken_barh([(x, 1)], (8 + y * 10, 4), color=color)
                # gnt.annotate(arrCPU[y], (x , 10 + 10 * y))
                plt.plot(label = 'Python')

    plt.savefig("gantt1.png") 
    f = Image.open("gantt1.png").show()
