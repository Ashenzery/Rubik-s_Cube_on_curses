import curses as curs

import numpy as np 


class Side:
  def __init__(self, color, position, size):

    self.ceils = np.array([[color] * size for x in range(size)])

    self.position = position




def conter_clockwise_rotacion(arr):

  return np.rot90(arr)



def clockwise_rotacion(arr):

  return np.rot90(arr, k=-1)



'''    

print Side("red", 'test', 3).ceils
print 
Side("cyan", 'test', 5).ceils

'''



colors = ['cyan' ,'red', 'green', 'yellow', 'blue', 'magenta']

positions = ['top', 'bottom', 'left', 'right', 'front', 'back']



cube = [Side(colors[_], positions[_], 3) for _ in range(6)]



'''

for side in cube:

  print side.ceils[1][1], side.position

'''




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

raw_input('')