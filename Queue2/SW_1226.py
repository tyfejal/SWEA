from collections import deque
for testcase in range(1,11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    y,x = -1,-1
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                y = i
                x = j
                break
        if y!=-1 or x!=-1:
            break
    q = deque()
    q.append((y,x,0))
    ret = 0
    used = [[0]*16 for _ in range(16)]
    directx = [-1,1,0,0]
    directy = [0,0,-1,1]
    while q:
        y,x,cnt = q.popleft()
        for i in range(4):
            dy = y+directy[i]
            dx = x+directx[i]
            if dy<0 or dx<0 or dy==len(arr) or dx==len(arr):continue
            if arr[dy][dx] == 1: continue
            if used[dy][dx] == 1: continue
            if arr[dy][dx] == 3:
                ret = cnt
                break
            q.append((dy,dx,cnt+1))
            used[dy][dx] = 1
        if ret!=0:
            break
    if ret>0: print(f'#{testcase}', 1)
    else: print(f'#{testcase}', 0)