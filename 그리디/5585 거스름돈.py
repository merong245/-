n = int(input())
n = 1000-n
coins = [500,100,50,10,5,1]
ans = 0
for coin in coins:
    ans += n//coin
    n %= coin

print(ans)
    
