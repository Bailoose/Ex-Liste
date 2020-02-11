lst = []
pos = 1
pos2 = pos-1
from random import *
for i in range(20):
  x = randint(5, 100)
  lst.append(x)
print(lst)

def maximum(liste):
  max = liste[0]
  i = 0
  imax = 0
  for el in liste:
    #print('el = ',el)
    if max < el: 
      max = el 
      imax = i
      #print('max = ',max )
    i = i+1
  return max,imax

print(maximum(lst)[1])

