import sys
sys.stdin = open("09_input.txt", "rt")

# 규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
# 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다. 
# N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램
# 을 작성하시오

# 최대값 찾는거. 굳이 리스트에 넣지 않아도 할 수 있다.
n = int(input())
price_list = []
for i in range(n):
    a, b, c = map(int, input().split())
    if a==b and b==c:
        price_list.append(10000 + a * 1000)
    elif a==b or b==c or a==c:
        if(a==b or a==c):
            price_list.append(1000 + a * 100)
        if(b==c):
            price_list.append(1000 + b * 100)
    else:
        price_list.append(max(a,b,c) * 100)

print(max(price_list))