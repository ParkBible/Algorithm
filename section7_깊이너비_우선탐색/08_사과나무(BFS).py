import sys
from collections import deque
sys.stdin = open("08_input.txt")

# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 
# 있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사
# 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 
# 남겨놓는다.

# 첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20) 
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 
# 이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
# 각 격자안의 사과의 개수는 100을 넘지 않는다.

# 수확한 사과의 총 개수를 출력합니다.

# 중심좌표를 처음에 큐에 넣어놓고 시작한다.
# 상하좌우(4갈래)로 뻗는다.
# 탐색한 곳은 체크를 한다.
# 

n = int(input())
apples = list()

for i in range(n):
    apples.append(list(map(int, input().split())))

pos = [n // 2, n // 2]
ch = [[0] * n for _ in range(n)]    # ch = [[0] * n] * n 은 얕은 복사로 처리됨
ch[pos[0]][pos[1]] = 1    # 이 작업에서 문제 발생

count = apples[pos[0]][pos[1]]

dQ = deque()
dQ.append(pos)
L = 0    # n // 2 - 1레벨의 트리까지만 돌아야 마름모가 만들어짐.

while dQ:
    up = 0
    down = 1
    left = 2
    right = 3

    if L == n // 2:
        break

    for i in range(len(dQ)):
        now = dQ.popleft()

        for direction in (up, down, left, right):
            x = now[0]
            y = now[1]

            if direction == up:
                y -= 1
            elif direction == down:
                y += 1
            elif direction == left:
                x -= 1
            else:
                x += 1

            if ch[x][y] == 0:
                dQ.append([x, y])
                ch[x][y] = 1
                count += apples[x][y]
        
    L += 1
    
for x in ch:
    print(x)

print(count)