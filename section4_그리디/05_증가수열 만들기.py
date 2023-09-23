import sys
from collections import deque
sys.stdin = open('05_input.txt')

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


# res_nums는 사실상 마지막 요소의 조회에만 필요하므로 굳이 리스트를 쓸 필요 없이 마지막 요소 하나만을 담은 last라는 변수 하나로 가능하다.

# 모범답안 : 포인터 2개(왼쪽, 오른쪽)를 두고, 왼쪽을 택했다면 왼쪽 포인터를 한 칸 옮기고, 오른쪽을 택했을 땐 마찬가지로 작업.
# tmp라는 리스트에 (값, "L or R") 을 넣고 정렬한 후 첫 번째 요소를 택하는 방법.

# lt = 0
# rt = length - 1
# last = 0
# res = ""
# tmp = []

# while lt <= rt:
#     if nums[lt] > last:
#         tmp.append((nums[lt], "L"))
#     if nums[rt] > last:
#         tmp.append((nums[rt], "R"))

#     tmp.sort()    # 튜플의 첫 번째 요소를 기준으로 정렬

#     if len(tmp) == 0:
#         break
#     else:
#         res = res + tmp[0][1]
#         last = tmp[0][0]
#         if tmp[0][1] == "L":
#             lt += 1
#         else:
#             rt -= 1
#     tmp.clear()