import copy


def monster_copy():
    global grid
    return copy.deepcopy(grid)


def next_pos(x, y, now_d):
    # 반시계
    for c_d in range(8,0,-1):
        nd = (now_d + c_d + 8) % 8
        nx, ny = x + dxs[nd], y + dys[nd]

        # 범위 안 , 시체 없고, 팩맨이 없는 경우
        if 1 <= nx < 5 and 1 <= ny < 5 and (nx, ny) != (px, py) and not graves[nx][ny]:
            return (nx, ny, nd)

    # 한바퀴 다돈 경우
    return (x, y, now_d)


def monster_move():
    global grid
    new_grid = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(5)]

    for i in range(1, 5):
        for j in range(1, 5):
            for md in range(8):
                x, y, nd = next_pos(i, j, md)
                new_grid[x][y][nd] += grid[i][j][md]

    grid = copy.deepcopy(new_grid)


def packman_move():
    global px, py, grid
    result = -1
    result_route = []
    # print(px,py)

    # 가장 많이 먹는 경로 찾기
    for route in packman_routes:
        nx, ny = px, py
        temp = 0
        # 정상 경로인지 확인
        flag = True

        visited = [[False for _ in range(5)] for _ in range(5)]
        for pd in route:
            nx, ny = pdxs[pd] + nx, pdys[pd] + ny
            # 격자 안으로 이동한 경우
            if 1 <= nx < 5 and 1 <= ny < 5:
                if visited[nx][ny]:
                    continue
                temp += sum(grid[nx][ny])
                visited[nx][ny] = True
            # 격자 밖으로 이동한 경우 새로운 경로
            else:
                flag = False
                break
        # 가장 많이 먹는 경우
        if flag and temp > result:
            result = temp
            result_route = route

    # 가장 많이 먹는 경로로 이동
    for pd in result_route:
        px, py = px + pdxs[pd], py + pdys[pd]

        if sum(grid[px][py]):
            for j in range(8):
                grid[px][py][j] = 0
            graves[px][py] = 3


def remove_graves():
    for i in range(1, 5):
        for j in range(1, 5):
            if graves[i][j]:
                graves[i][j] -= 1


def monster_copy_done():
    for x in range(1, 5):
        for y in range(1, 5):
            for k in range(8):
                grid[x][y][k] += copied_monster[x][y][k]


def set_packman_routes(route):
    if len(route) == 3:
        packman_routes.append(route)
        return

    for i in range(4):
        set_packman_routes(route + [i])


def count_monster():
    ans = 0
    for i in range(1, 5):
        for j in range(1, 5):
            ans += sum(grid[i][j])
    print(ans)


m, t = map(int, input().split())
graves = [[0 for _ in range(5)] for _ in range(5)]
# 방향의 몬스터 수
grid = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(5)]
packman_routes = []

for _ in range(m):
    r, c, d = map(int, input().split())
    grid[r][c][d - 1] += 1

px, py = map(int, input().split())
# 물고기 방향은 좌시작 시계방향
dxs, dys = [0, -1, -1, -1, 0, 1, 1, 1], [-1,-1,0,1,1,1,0,-1]
# 팩맨 방향은 상좌하우
pdxs, pdys = [-1, 0, 1, 0], [0, -1, 0, 1]

# 팩맨 경로 구하기
set_packman_routes([])

# print("초기 몬스터")
# print(*grid,sep='\n',end='\n\n')
for _ in range(t):
    # 몬스터 복제

    copied_monster = monster_copy()
    # 몬스터 이동
    monster_move()
    # print("몬스터 이동")
    # print(*grid,sep='\n',end='\n\n')

    # 팩맨 이동
    packman_move()
    # print("팩맨 이동")
    # print(*grid,sep='\n',end='\n\n')

    # 몬스터 시체 소멸
    remove_graves()
    # print(*graves,sep='\n',end='\n\n')

    # 몬스터 복제 완성
    monster_copy_done()

    # print("몬스터 복제")
    # print(*grid,sep='\n',end='\n\n')

count_monster()