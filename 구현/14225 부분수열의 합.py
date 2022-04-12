n = int(input())
nums = sorted(list(map(int,input().split())))

ans = set()
def choose(curr, li):
    if curr == n:
        ans.add(sum(li))

    else:
        choose(curr+1, li+[nums[curr]])
        choose(curr+1, li+[0])
choose(0,[])
cnt = 1
while True:
    if cnt not in ans:
        print(cnt)
        break
    cnt+=1
        
