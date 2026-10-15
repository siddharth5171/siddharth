def slowfast(te):
    slow=0
    fast=0
    while fast<len(te)-1 and fast+1<len(te)-1:
            slow+=1
            fast+=2

    return te[slow]
te=[1,2,3,4,5,6]
print(slowfast(te))

