# arr=[10,20,30,40,50]
# print(arr)
# print(type(arr))
# for i in range(len(arr)):
#     print(i, arr[i]) 

#sum array
# arr=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in range(len(arr)):
#     sum=sum+arr[i]
# print("sum of array:",sum)  


#find max and min in array

# arr=[10,23,45,67,89,90]
# max=arr[0]
# min=arr[0]
# for i in range(1, len(arr)):
#     if arr[i]>max:
#         max=arr[i]
#     elif arr[i]<min:
#         min=arr[i]
# print("max value in array:",max)
# print("min value in array:",min)   

# arr=[10,20,30,40,50]
# max=arr[-5]
# min=arr[-5]
# for i in range(-4,0):
#     if arr[i]>max:
#         max=arr[i]
#     elif arr[i]<min:
#         min=arr[i]
# print("max value in array:",max)
# print("min value in array:",min)


# slicing
# arr=[10,20,30,40,50]
# print(arr[0:3])  #10,20,30
# print(arr[1:4])  #20,30,40
# print(arr[2:])   #30,40,50
# print(arr[1:-1])
# print(arr[-4:-1])  #20,30,40

# arr=[10,20,30,40,50]
# print(arr[0:3])  #10,20,30
# print(arr[-5:-2])  #10,20,30
# print(arr[0:-2])  #10,20,30
# print(arr[-5:3])  #10,20,30

# arr=[10,20,30,[40,50,60]]
# for i in range(len(arr)):
#     print(i,arr[i])
# print(arr[2:])  #30,[40,50,60]
# print(arr[3])
# print(arr[3][0:2])  #40

# arr=[10,20,30,[40,50,60]]
# arr[0]=5
# arr.reverse()
# print(arr)  #[[40,50,60],30,20,5]

# arr=[10,20,30,40,50]
# res=[]
# for i in range(len(arr)):
#     res.append(arr[i])
# print(res)  #[20,40,60,80,100]  


# arr=[10,20,30,40,50]
# arr1=[11,12,13,14,15]
# res=arr+arr1
# print(res)  #[10,20,30,40,50,11,12,13,14,15]

# arr=[121,12,11,13,188,112]
# res=sorted(arr)
# print(res)  #[11,12,13,121,112,188]

# 10 replace with 100
arr=[10,20,30,40,10,11,23,10]
for i in range(len(arr)):
    if arr[i]==10:
        arr[i]=100
print(arr)  #[100,20,30,40,100,11,23,100]   
