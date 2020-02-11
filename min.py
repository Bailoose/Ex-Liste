lst = []
pos = 1
pos2 = pos-1
from random import *
for i in range(20):
  x = randint(5, 100)
  lst.append(x)
print(lst)


def minimum(liste):
  min = liste[0]
  i = 0
  imin = 0
  for el in liste:
    #print('el = ',el)
    if min > el: 
      min = el 
      imin = i
      #print('max = ',max )
    i = i+1
  return min,imin



print(minimum(lst))
