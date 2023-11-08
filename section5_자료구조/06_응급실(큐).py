import sys
sys.stdin = open("06_input.txt")

# 이 바보야 진짜 아니야ㅏ~~~~~~
# 메디컬 병원 응급실에는 의사가 한 명밖에 없습니다.
# 응급실은 환자가 도착한 순서대로 진료를 합니다. 하지만 위험도가 높은 환자는 빨리 응급조치를 해야 합니다. 
# 이런 문제를 보완하기 위해 응급실은 다음과 같은 방법으로 환자의 진료순서를 정합니다.
# • 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼냅니다.
# • 나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로 다시 넣습니다. 그렇지 않으면 진료를 받습니다.
# 즉 대기목록에 자기 보다 위험도가 높은 환자가 없을 때 자신이 진료를 받는 구조입니다.

# 현재 N명의 환자가 대기목록에 있습니다.
# N명의 대기목록 순서의 환자 위험도가 주어지면, 대기목록상의 M번째 환자는 몇 번째로 진료를 받는지 출력하는 프로그램을 작성하세요.
# 대기목록상의 M번째는 대기목록의 제일 처음 환자를 0번째로 간주하여 표현한 것입니다.

# 첫 줄에 자연수 N(5<=N<=100)과 M(0<=M<N)이 주어집니다.
# 두 번째 줄에 접수한 순서대로 환자의 위험도(50<=위험도<=100)가 주어집니다.(같은 위험도 존재 가능)

from collections import deque

n, m = map(int, input().split())
dq = list(map(int, input().split()))
dq = deque(dq)

order = 0

while dq:
    p = dq.popleft()
    m -= 1

    if m == -1:
        if len(dq) == 1 or p >= max(dq):
            order += 1
            print(order)
            break
        else:
            m = len(dq)
            dq.append(p)
    else:
        if p >= max(dq):
            order += 1
        else:
            dq.append(p)
            

# 모범답안
# dq를 (인덱스, 값)의 튜플 형태로 만든다.

# dq = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
# dq = deque(dq)
# cnt = 0
# while True:
#     cur = dq.popleft()
    
#     if any(cur[1] < x[1] for x in dq):
#         dq.append(cur)
#     else:
#         cnt += 1
#         if cur[0] == m:
#             break

# print(cnt)