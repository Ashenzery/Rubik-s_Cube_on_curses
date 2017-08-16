import curses as curs
import numpy as np



def make_side(color, size):
    return np.array([[color] * size for x in range(size)])

def conter_clockwise_rotacion(arr):
    return np.rot90(arr)

def clockwise_rotacion(arr):
    return np.rot90(arr, k=-1)



print make_side("red",  3)
print
print
print make_side("cyan", 5)
print
print
print

colors = ['cyan' ,'red', 'green', 'yellow', 'blue', 'magenta']
positions = ['top', 'bottom', 'left', 'right', 'front', 'back']
cube = { positions[_] : make_side(colors[_], 3) for _ in range(6) }

for key, val in cube.items():
    print key, val[1][1]
print
print

cube['top'], cube['bottom'] = cube['bottom'], cube['top']

for key, val in cube.items():
    print key, val[1][1]
print
print
'''
from copy import deepcopy
num = [[1+i*3, 2+i*3, 3+i*3] for i in range(3)]
num = np.array(num)
print num
print
print conter_clockwise_rotacion(deepcopy(num))
print
print clockwise_rotacion(deepcopy(num))
'''
