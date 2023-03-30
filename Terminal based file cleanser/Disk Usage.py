import psutil
from blessings import Terminal


term=Terminal()

width=term.width
height=term.height



def barGraph(percent):
    graphWidth=int(percent*(width-15))
    return '['+'#' * graphWidth+' ' * (width-10-graphWidth) + ']'

while True:
    with term.fullscreen():
        mem = psutil.disk_usage('/')
        used_percent = mem.percent

        print(term.clear())
        print(term.move(0, 0))

        print('Disk Usage: {}%'.format(used_percent))
        print(barGraph(used_percent / 100))

        psutil.cpu_percent(interval=10)

        if term.inkey() is not None:
            break
