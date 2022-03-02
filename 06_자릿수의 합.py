import sys
sys.stdin = open("06_input.txt", "rt")

# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
# 하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수 def digit_sum(x)를 
# 꼭 작성해서 프로그래밍 하세요.

# 다른 답안 : x가 0보다 클 때까지 res 변수에 x%10 값을 계속 더한다. 125면 5 + 2 + 1 이런 식.
# while x > 0:
#    sum += x % 10
#    x = x // 10

def digit_sum(x):
    x = str(x)
    res = 0
    for i in range(len(x)):    # 그냥 for i in str(x) 로도 가능.
        res += int(x[i])
    return res

n = int(input())
num_list = list(map(int, input().split()))
max_num = 0
max_idx = 0
for idx, x in enumerate(num_list):
    digit_res = digit_sum(x)
    if(max_num < digit_res):
        max_num = digit_res
        max_idx = idx

print(num_list[max_idx])