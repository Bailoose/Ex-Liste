lst = []
tri = []
from random import *
for i in range(20):
  x = randint(0, 20)
  lst.append(x)
print(lst)

def minimum(liste):

    min = liste[0]
    i = 0
    imin = 0
    for el in liste:
   #print('el = ',el))
        if min > el:
          min = el
          imin = i
          #print('max = ',max )
        i = i+1
    return min,imin

n = len(lst)

for i in range(n):
    #print(minimum(lst))
    tri.append(minimum(lst)[0])
    del lst[(minimum(lst)[1])]


print(tri)
