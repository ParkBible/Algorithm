import sys
sys.stdin = open("10_input.txt", "rt")

# 1번 문제가 맞는 경우에는 1점으로 계산한다. 앞의 문제에 대해서는 답을 틀리다가 
# 답이 맞는 처음 문제는 1점으로 계산한다. 또한, 연속으로 문제의 답이 맞는 경우에서 두 번째 
# 문제는 2점, 세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산한다. 틀린 문제는 0점으로
# 계산한다. 시험문제의 채점 결과가 주어졌을 때, 총 점수를 계산하는 프로그램을 작성하시오.

n = int(input())
res_list = list(map(int, input().split()))

total_score = 0
plus_score = 1
for i in res_list:
    if i==1:
        total_score += plus_score
        plus_score += 1
    else:
        plus_score = 1

print(total_score)