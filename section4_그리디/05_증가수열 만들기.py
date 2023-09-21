import sys
from collections import deque
# sys.stdin = open("05_input.txt")

# 1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다. 
# 이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열
# 을 만듭니다. 이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니다.
# 예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다.
# 맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4, 
# 왼쪽 끝에서 5를 가져와 2 3 4 5 증가수열을 만들 수 있습니다.

# 첫째 줄에 최대 증가수열의 길이를 출력합니다.
# 두 번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 ‘L', 오른쪽 끝에서 가져갔으면 ’R'를
# 써간 문자열을 출력합니다.(단 마지막에 남은 값은 왼쪽 끝으로 생각합니다.)

# 정리하면 작은 숫자가 이득이지만 현재 수열에 들어있는 마지막 요소보다는 커야 함.
length = input()
nums = list(map(int, input().split()))

res_nums = []
results = []

for i in range(len(nums)):
    if len(nums) == 1:
        if nums[0] > res_nums[-1]:
            results.append("L")
    if i == 0:
        if nums[0] < nums[-1]:
            res_nums.append(nums.pop(0))
            results.append("L")
        else:
            res_nums.append(nums.pop(-1))
            results.append("R")
    else:
        if nums[0] < res_nums[-1] and nums[-1] < res_nums[-1]:
            break

        if nums[0] < nums[-1] and nums[0] > res_nums[-1]:
            res_nums.append(nums.pop(0))
            results.append("L")
        else:
            if res_nums[-1] < nums[-1]:
                res_nums.append(nums.pop(-1))
                results.append("R")
            else:
                res_nums.append(nums.pop(0))
                results.append("L")
            

print(len(results))
print("".join(results))