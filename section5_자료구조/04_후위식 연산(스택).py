import sys
sys.stdin = open("04_input.txt")

# 후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
# 만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 12입니다

# 숫자를 스택에 쌓아놓고, 연산자가 나오면 계산한 뒤 계산 결과를 다시 스택에 추가한다.
# 하지만 -나 /의 연산은 계산 결과가 숫자보다 앞에 나와야 한다.
# ex) 1+3-2라면 1+3=4가 스택에 먼저 들어가고, 2가 나중에 들어가기 때문에 pop 순서를 생각하면 순서가 2,4가 되지만 연산은 4-2가 되어야 한다.

text = list(map(str, input()))
stack = []

for t in text:
    if t.isdecimal():
        stack.append(t)
    else:
        if len(stack) == 2:
            stack.reverse()

        cal = str(stack.pop()) + t + str(stack.pop())
        stack.append(eval(cal))
        

print(stack[0])

# 모범답안

# if len(stack) == 2:
#     stack.reverse()

# 대신에

# n2 = str(stack.pop())
# n1 = str(stack.pop())

# 를 정의하여 n2 - n1이 되도록 함.