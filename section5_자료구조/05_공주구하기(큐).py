import sys
sys.stdin = open("05_input.txt")

# 정보 왕국의 이웃 나라 외동딸 공주가 숲속의 괴물에게 잡혀갔습니다. 
# 정보 왕국에는 왕자가 N명이 있는데 서로 공주를 구하러 가겠다고 합니다. 정보왕국의 왕은 
# 다음과 같은 방법으로 공주를 구하러 갈 왕자를 결정하기로 했습니다.
# 왕은 왕자들을 나이 순으로 1번부터 N번까지 차례로 번호를 매긴다. 
# 그리고 1번 왕자부터 N번 왕자까지 순서대로 시계 방향으로 돌아가며 동그랗게 앉게 한다. 
# 그리고 1번 왕자부터 시계방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다.
# 한 왕자가 K(특정숫자)를 외치면 그 왕자는 공주를 구하러 가는데서 제외되고 원 밖으로 나오게 된다.
# 그리고 다음 왕자부터 다시 1부터 시작하여 번호를 외친다.
# 이렇게 해서 마지막까지 남은 왕자가 공주를 구하러 갈 수 있다.

# 첫 줄에 자연수 N(5<=N<=1,000)과 K(2<=K<=9)가 주어진다.
# 첫 줄에 마지막 남은 왕자의 번호를 출력합니다.

# 리스트를 만들고, k번까지 pop하고, k번 앞의 번호는 뒤로 이어붙임.

n, k = map(int, input().split())
queue = list(range(1, n + 1))

cnt = 0

while len(queue) != 1:
    if cnt < k - 1:
        cnt = cnt + 1
        queue.append(queue.pop(0))
    elif cnt == k - 1:
        cnt = 0
        queue.pop(0)

print(queue[0])


# 모범답안
# deque 자료구조를 통해 가장 왼쪽 인덱스를 빼내는 것에 popleft() 메소드를 사용한다.

# from collections import deque
# dq = list(range(1, n + 1))
# dq = deque(dq)

# while dq:
#     for _ in range(k-1):
#         dq.append(dq.popleft())
#     dq.popleft()

#     if len(dq) == 1:
#         print(dq[0])
#         dq.popleft()