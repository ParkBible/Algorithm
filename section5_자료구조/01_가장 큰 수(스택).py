import sys
sys.stdin = open("01_input.txt")

# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다. 
# 여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
# 만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다. 

num, del_count = map(int, input().split())
nums = list(map(int, str(num)))

# 7개 중 3개를 제거해야 한다면 선택할 수 있는 숫자는 4개
# 5, 2, 7, 6 중 가장 큰 숫자를 선택해야 한다.
# 그 다음은 6, 8 중 가장 큰 숫자 선택.

# 접근법 : 숫자 각각은 자신 앞에 자신보다 작은 숫자가 있으면 그 숫자를 지워버린다. 하지만 지우는 횟수는 한정되어있음.
# 리스트의 append와 pop으로 스택 자료구조를 구현한다.

# count = 0
# result = []

# for i in range(len(nums)):
#     if count == del_count:
#         break

#     num = nums.pop(0)
#     result.append(num)

#     if i > 0:
#         if nums[i + 1] > result[-1]:
#             result.pop()
#             count += 1

# 모범답안 : while result가 조건이라면, result가 비어 있지 않다면 참.
# 리스트가 비어 있지 않고, del_count 횟수가 남았고, result의 마지막 요소가 현재 숫자보다 작다면 result에서 빼버림.

result = []

for x in nums:
    while result and del_count > 0 and x > result[-1]:
        result.pop()
        del_count -= 1

    result.append(x)

if del_count > 0:
    result = result[:-del_count]

print("".join(map(str, result)))