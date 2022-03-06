import sys
sys.stdin = open("13_input.txt", "rt")

# 다음과 같은 규칙으로 카드의 위치를 바꾼다: 구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면
# 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.

card_list = [x for x in range(1, 21)]
print(card_list)

temp = 0
for i in range(10):
    start, stop = map(int, input().split())
    #print(start, stop)
    for j in range(start+1, stop+2):
        #temp = card_list[9]
        #card_list[9] = card_list[4]
        #card_list[4] = temp
        print(j)