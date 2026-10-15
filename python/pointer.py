def twosum(arr,target):
    left=0
    right=len(arr)-1

    while left<right:
        sum1=arr[left]+arr[right]
        if sum1==target:
            return left,right
        elif sum1<target:
            left+=1
        else:
            right-=1

    return -1


arr=[2,4,7,11,30]
target=18
print(twosum(arr,target))