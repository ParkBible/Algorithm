import sys
sys.stdin = open("03_input.txt")

# 후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
# 예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
# 3+5*2/(7-2)는 352*72-/+ 가 된다.

# 1) 스택엔 연산자와 여는 괄호만 넣는다. 숫자는 바로 결과에 더한다.
# 2) 닫는 괄호를 만나면 여는 괄호까지의 스택을 모두 토해내고 결과에 더한다. 여는 괄호는 결과에 더하지 않는다.
# 3) 자신보다 높은 서열의 연산자를 만나면 스택에 추가한다.
# 4) 자신과 같거나 낮은 서열의 연산자를 만나면 스택을 모두 토해내고 결과에 더한다. (여는 괄호 제외)
# 5) 모든 문자를 돌고 마지막까지 스택에 남은 연산자를 결과에 더한다.

text = input()
stack = []
result = ""

rank = {"(": 0, "*": 1, "/": 1, "+": 2, "-": 2}

for t in text:
    if t.isdecimal():
        result += t
    else:
        if t == ")":
            while stack:
                temp = stack.pop()
                
                if temp == "(":
                    break

                result += temp
            continue
        if len(stack) == 0 or rank.get(stack[-1]) > rank.get(t) or stack[-1] == "(":
            stack.append(t)
        else:
            while stack:
                if stack[-1] == "(":
                    break
                result += stack.pop()
            stack.append(t)
    
while stack:
    result += stack.pop()

print(result)


# 모범답안
# 문자열을 순회하며 만날 수 있는 모든 경우에 대해 명확하게 조건을 분기하고 있음. (나처럼 결과론적이지 않다...)
# 여는 괄호일땐 무조건 스택에 추가한다.
# *나 /를 만났다면 스택에서 *나 /만 결과로 토해낸다.
# +나 -를 만났다면 스택을 모두 결과로 토해낸다.(여는 괄호 전까지)
# 닫는 괄호를 만났다면 여는 괄호 전까지 모두 결과로 토해내고, 여는 괄호는 스택에서 제거한다.

# for t in text:
#     if t.isdecimal():
#         result += t
#     else:
#         if t == "(":
#             stack.append()
#         elif t == "*" or t == "/":
#             while stack and (stack[-1] == "*" or stack[-1] == "/"):
#                 result += stack.pop()
#             stack.append()
#         elif t == "+" or t == "-":
#             while stack and stack[-1] != "(":
#                 result += stack.pop()
#             stack.append()
#         elif t == ")":
#             while stack and stack[-1] != "(":
#                 result += stack.pop()
#             stack.pop()

# while stack:
#     result += stack.pop()

# print(result)