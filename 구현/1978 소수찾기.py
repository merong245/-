n= int(input())
nums = list(map(int,input().split()))

cnt = 0
if 1 in nums:
    cnt = 1
for num in nums:
    for i in range(2,num):
        if num%i == 0:
            cnt+=1
            break
print(len(nums)- cnt)
