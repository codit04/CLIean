import psutil
from blessings import Terminal

term = Terminal()

width = term.width
height = term.height

def draw_bar_graph(percent):
    bar_width = int(percent * (width - 10))
    return '[' + '#' * bar_width + ' ' * (width - 10 - bar_width) + ']'

while True:

    with term.fullscreen():
        # Get current memory usage
        mem = psutil.virtual_memory()
        used_percent = mem.percent

        print(term.clear())
        print(term.move(0, 0))

        print('Memory Usage: {}%'.format(used_percent))
        print(draw_bar_graph(used_percent / 100))

        psutil.cpu_percent(interval=10)

        if term.inkey() is not None:
            break
