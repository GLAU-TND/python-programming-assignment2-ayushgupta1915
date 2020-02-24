def maxConsecutiveOnes(x):
    c=0
    while (x!=0):
        x=(x&(x<<1))
        c=c+1
    return c
print(maxConsecutiveOnes(int(input())))
