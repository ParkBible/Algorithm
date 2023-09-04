import sys
sys.stdin = open("02_input.txt", "rt")

# 현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습
# 니다. 현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
# 현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
# “다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자만 뽑기로 했습니다.”
# 만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니다.

num = int(input())
candidates = []

for _ in range(num):
    candidates.append(list(map(int, input().split())))

count = num

for i in range(num):
    for j in range(num):
        if (i != j and candidates[i][0] < candidates[j][0] and candidates[i][1] < candidates[j][1]):
            count = count - 1
            break

print(count)

# 모범답안 접근법 : 키순으로 내림차순 정렬 후, for문 안에서 몸무게의 최댓값이 갱신될때만 카운팅함.
# 키순으로 내림차순 정렬되었으니 다음 인덱스가 선발되려면 무조건 몸무게라도 커야한다는 원리

# candidates.sort(reverse=True)

# max_weight = 0
# count = 0

# for height, weight in candidates:
#     if weight > max_weight:
#         max_weight = weight
#         count = count + 1

# print(count)