s = input().rstrip()
t = input().rstrip()
answer = 0

def choose(string):
    global answer

    if len(s) == len(string):
        if s == string:
            answer = 1
        return
    if len(string) < 0:
        return
    if string[-1] == 'A':
        choose(string[:-1])
    if string[0] == 'B':
        choose(string[1:][::-1])

choose(t)
print(answer)