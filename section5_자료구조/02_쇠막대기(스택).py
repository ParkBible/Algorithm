import sys
sys.stdin = open("02_input.txt")

# 1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
# 2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다.
# 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하시오.

sticks = input()

# 내 생각 : 큰 괄호 안에 ()가 몇 개가 있는지 파악하면 조각의 개수를 알 수 있을 것...
# 과정은 다음과 같음. () -> .로 변경

# ()(((()())(())()))(())

# .(((..)(.).))(.)
#     9   4 2   2
# 1) .이 나올 때까지 (를 계속 스택에 쌓는다.
# 2) .이 나오는 순간 조각 개수 * 2를 결과에 더한다. 연달아 나오는지를 알아야 하니까 .도 스택에 쌓는다.
# 3) .이 연달아 나올때마다 조각 개수 * 1를 결과에 더한다.
# 4) )가 나오면 (를 하나 pop한다.
# 5) (가 하나도 없다면 스택에서 .을 모두 제거한다.

# sticks = sticks.replace("()", ".")
# sticks = list(map(str, sticks))

stack = []
result = 0

# for stick in sticks:
#     if stick == "(":
#         stack.append(stick)
#     elif stick == ".":
#         if len(stack) > 0:
#             if stack[-1] == "(":
#                 result += stack.count("(")
#             else:
#                 result += stack.count("(") * 2
            
#         stack.append(stick)
#         if len(stack) == 1:
#             stack.pop()
#     else:
#         stack.remove("(")
#         if "(" not in stack:
#             while "." in stack:
#                 stack.remove(".")

# print(result)

# 결과 : 예제 문제는 답이 나왔으나 다른 예제에 대해서 실패

# 모범답안
# (가 나오면 스택을 쌓고 레이저인 )가 나오면 쌓인 스택 개수만큼 결과에 더함
# 레이저인지 아닌지 파악을 위해 )가 나올 땐 앞에 (가 있는지 확인함
# 레이저가 아닌 )가 있을 땐 무조건 결과 + 1 (마지막 조각)
# )가 나오면 스택 - 1

# 알고리즘을 짜기 쉬운 규칙을 찾는 데 집중하자!!

for i in range(len(sticks)):
    if sticks[i] == "(":
        stack.append(sticks[i])
    else:
        stack.pop()
        if sticks[i - 1] == "(":
            result += len(stack)
        else:
            result += 1

print(result)