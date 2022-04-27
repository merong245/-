import sys
input =sys.stdin.readline

n =int(input())

a = input()

# 연산자 우선순위 동일 -> 왼쪽 순서부터 계산
# 괄호안에는 연산자 하나
# 중첩괄호 불가

def cal(a):
    res = 0
    op = ''
    cnt = 0
    
    for i in range(len(a)):
        tmp = a[i]
        if cnt:
            cnt -= 1
            continue
        
        if '0' <= tmp <= '9' or tmp == '(':
            
            if tmp == '(':
                tmp = cal(a[i+1:i+4])
                cnt=4
            if i == 0:
                res = int(tmp)
            else:
                if op == '*':
                    res = res*int(tmp)
                elif op == '-':
                    res = res-int(tmp)
                elif op == '+':
                    res = res+int(tmp)
        else:
            op = tmp
    return res

ans = -sys.maxsize
def simulate(curr, a):
    global ans
    if curr >= len(a):
        ans = max(cal(a),ans)
        return
    
        
    # 0123     012345
    # 1*2+ - > (1*2)+
    simulate(curr+2, a)
    simulate(curr+6, a[:curr] + '(' + a[curr:curr+3]+')' + a[curr+3:])    
simulate(0,a)
print(ans)
