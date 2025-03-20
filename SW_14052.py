from collections import deque

T = int(input())
for testcase in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    y,x = 0,0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                y = i
                x = j

    q= deque()
    q.append((y,x,0))

    ret = 0
    visited = [[0]*n for _ in range(n)]
    directy = [0,0,1,-1]
    directx = [1,-1,0,0]
    while q:
        y,x,cnt = q.popleft()
        for i in range(4):
            dy = y+directy[i]
            dx = x+directx[i]
            if dy<0 or dy>=n or dx<0 or dx>=n:continue
            if arr[dy][dx] == 1: continue
            if visited[dy][dx] ==1 : continue
            if arr[dy][dx] == 3:
                ret = cnt
                break
            q.append((dy,dx,cnt+1))
            visited[dy][dx] = 1
        if ret != 0: break

    print(f'#{testcase} {ret}')