n= int(input())

divider = 2

while n!=1:
    if n%divider==0:
        n = n//divider
        print(divider)
    else:
        divider+=1
