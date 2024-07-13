import sys
from collections import deque
sys.stdin = open("09_input.txt")

#  7*7 격자판 미로를 탈출하는 최단경로의 경로수를 출력하는 프로그램을 작성하세요. 경로수는 
# 출발점에서 도착점까지 가는데 이동한 횟수를 의미한다. 출발점은 격자의 (1, 1) 좌표이고, 탈
# 출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 도로이다.
# 격자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면
# 위와 같은 경로가 최단 경로이며 경로수는 12이다. 

# 7*7 격자판의 정보가 주어집니다
# 첫 번째 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1를 출력한다.

mazeElements = []

for i in range(7):
    mazeElements.append(list(map(int, input().split())))

mazeElements[0][0] = 1    # 최초 위치

pos = [0, 0]    # 현재 위치
dis = [[0] * 7 for _ in range(7)]    # 거리 기록

dQ = deque()
dQ.append(pos)

directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]    # 상하좌우

while dQ:    
    now = dQ.popleft()
    x = now[0]
    y = now[1]

    for direction in directions:
        nextX = x + direction[0]
        nextY = y + direction[1]

        if 0 <= nextX <= 6 and 0 <= nextY <= 6 and mazeElements[nextX][nextY] == 0:
            mazeElements[nextX][nextY] = 1
            dQ.append([nextX, nextY])
            dis[nextX][nextY] = dis[x][y] + 1
        
print(dis[6][6])