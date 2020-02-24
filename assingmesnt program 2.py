ls=eval(input())
a=[]
from itertools import permutations
c=permutations(map(str,ls))
for i in c:
    num=''.join(i)
    a.append(num)
print(max(a))
