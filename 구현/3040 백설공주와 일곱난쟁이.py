import sys
input =sys.stdin.readline

people = []
for _ in range(9):
    people.append(int(input()))

ans = sum(people)
answer = False
for i in range(9):
    for j in range(i+1,9):
        if ans - people[i] - people[j] == 100:
            people.pop(j)
            people.pop(i)
            answer = True
            break
    if answer:
        break
            
    

print(*people, sep=" ")
    
    
    
    
