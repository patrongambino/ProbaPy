# app.py

import itertools 
  
listA = [1, 3, 4, 7]
perm = itertools.permutations(listA) 
  
for i in list(perm): 
    print(i)
