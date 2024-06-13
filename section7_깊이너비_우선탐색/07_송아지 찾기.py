import sys
from collections import deque
sys.stdin = open("07_input.txt")

# 현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다. 현수의 위치와 송아
# 지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과 
# 같은 방법으로 이동한다. 
# 현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 
# 있다. 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성
# 하세요.

# 첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000
# 까지이다.
# 점프의 최소횟수를 구한다.

MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
s, e = map(int, input().split())
ch[s] = 1    # 체크함
dis[s] = 0    # 거리 기록
dQ = deque()
dQ.append(s)

while dQ:
    now = dQ.popleft()    # 현재 나의 위치를 나타냄
    if now == e:
        break

    for next in (now - 1, now + 1, now + 5):    # 세 가지 경우에 대해 순회
        if 0 < next <= MAX:
            if ch[next] == 0:    # 방문하지 않은 위치일 경우
                dQ.append(next)    # 다음 위치를 큐에 추가함(즉, 이동함)
                ch[next] = 1    # 방문했다고 체크함
                dis[next] = dis[now] + 1    # 거리(레벨)가 하나 늘어남

print(dis[e])