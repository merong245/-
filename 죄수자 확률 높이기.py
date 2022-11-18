import random, math
# https://www.youtube.com/watch?v=PE4vLbyOgw0
for _ in range(3):
    n = 3000
    answer = 0
    for _ in range(n):
        boxes = [0] * 100
        cnt = 0
        while cnt != 100:
            rand = random.randrange(0, 100)
            if not boxes[rand]:
                boxes[rand] += cnt
                cnt += 1

        result = 0
        for i in range(100):
            now = i
            for _ in range(50):
                if boxes[now] == i:
                    result += 1
                    break
                else:
                    now = boxes[now]

        if result == 100:
            answer += 1

    print(answer / n)