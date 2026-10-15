arr = [100, 50, 70, 90, 150,500,200]
k = 3

window_sum = sum(arr[:k])
print(window_sum)
for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    print(window_sum)


# def wimdowsum(arr,days):
#     windowsum=0
#     for i in range(days):
#         windowsum+=arr[i]
#     print("number user visited",windowsum)

#     for i in range (1,len(arr)-days+1):
#         windowsum=windowsum-arr[i-1]+arr[i-days+1]
#         print(" number visites window",windowsum)
# arr = [100, 50, 70, 90, 150,500,200]
# days = 3
# print(windowsum(arr,days))