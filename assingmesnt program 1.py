l=list(map(str,input().split()))
x=[]
a=len(l)
for i in range(len(l)):
    for j in range(len(l)):
        if x[i][-1]==l[j][0]:
            x.append(l[j])
            l.remove(l[j])
            break
if a==len(x):
    print(x)
else:
    print("[]")
