import sys
sys.stdin = open("07_input.txt")

# 현수는 1년 과정의 수업계획을 짜야 합니다.
# 수업중에는 필수과목이 있습니다. 이 필수과목은 반드시 이수해야 하며, 그 순서도 정해져 있습니다.
# 만약 총 과목이 A, B, C, D, E, F, G가 있고, 여기서 필수과목이 CBA로 주어지면 필수과목은 
# C, B, A과목이며 이 순서대로 꼭 수업계획을 짜야 합니다.
# 여기서 순서란 B과목은 C과목을 이수한 후에 들어야 하고, A과목은 C와 B를 이수한 후에 들어야 한다는 것입니다. 
# 현수가 C, B, D, A, G, E로 수업계획을 짜면 제대로 된 설계이지만
# C, G, E, A, D, B 순서로 짰다면 잘 못 설계된 수업계획이 됩니다.
# 수업계획은 그 순서대로 앞에 수업이 이수되면 다음 수업을 시작하다는 것으로 해석합니다.
# 수업계획서상의 각 과목은 무조건 이수된다고 가정합니다.
# 필수과목순서가 주어지면 현수가 짠 N개의 수업설계가 잘된 것이면 “YES", 잘못된 것이면 
# ”NO“를 출력하는 프로그램을 작성하세요.

# 첫 줄에 한 줄에 필수과목의 순서가 주어집니다. 모든 과목은 영문 대문자입니다.
# 두 번째 줄에 N(1<=N<=10)이 주어집니다.
# 세 번째 줄부터 현수가 짠 N개의 수업설계가 주어집니다.(수업설계의 길이는 30이하이다)
# 수업설계는 같은 과목을 여러 번 이수하도록 설계해도 됩니다.

# 중요 : 같은 과목이 여러 개 있을 수 있다는 조건 때문에, 수업설계가 BCA인데 DBACA 이면 NO라는 결과가 나와야 함.

from collections import deque

order_text = input()
n = int(input())

for i in range(n):
    plan = input()
    plan = deque(plan)

    order = list(order_text)
    order = deque(order)

    while plan:
        el = plan.popleft()

        if el == order[0]:
            order.popleft()
            if len(order) == 0:
                print("#", i + 1, " YES")
                break
        elif el in order:
            break

    if len(order) > 0:
        print("#", i + 1, " NO")


# 모범답안
# 파이썬에서는 반복문에도 else를 사용할 수 있다. break로 도중에 중단되지 않고 모두 돌았다면 else를 탐.
# 내가 수강하고자 하는 과목이 설계에 포함되어 있는 과목이라면 설계에서 그 과목의 순서를 판단
# plan: TCDBA / order: CBA 라면, C를 만났을 때 C가 포함되어있으니 첫번째 if문을 통과함.
# 그리고 order에서도 첫번째 C이므로 두번째 if문은 통과하지 않음.

order = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(order)

    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i + 1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i + 1))
        else:
            print("#%d NO" %(i + 1))