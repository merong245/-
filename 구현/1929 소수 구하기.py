m ,n = map(int,input().split())

nums = [i for i in range(10000001)]
nums[1] = 0
for i in range(2,n):
    if nums[i] == 0:
        continue
    for j in range(i*2, n+1,i):

        nums[j] = 0
    
for i in range(m,n+1):
    if nums[i] != 0:
        print(nums[i])
