import sys
sys.stdin = open("01_input.txt", "rt")

# 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들
# 려고 한다. 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하
# 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 단, 회의는 한번 시작하면 중간에 중
# 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 첫째 줄에 최대 사용할 수 있는 회의 수를 출력하여라.

# 팁: 회의를 최대한 많이 해야 하므로, 끝나는 시간을 기준으로 회의들을 정렬해야 한다.
# 회의 끝나는 시간과 비교해 다음 회의의 시작 시간이 그 이전이면 그 회의는 못하는거

n = int(input())
meetings = []
results = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))

# x는 meetings의 요소
meetings.sort(key=lambda x: (x[1], x[0]))

# 회의 개수만 구하는 문제이므로 count 변수에만 기록해놓아도 상관없음.
for i, meeting in enumerate(meetings):
    if i == 0:
        results.append(meeting)
        continue

    if meeting[0] >= results[-1][1]:
        results.append(meeting)

print(len(results))


# 모범답안 (요소가 리스트인 for문 돌릴때의 변수에 주목)
# end_time = 0
# count = 0
# for start, end in meetings:
#     if start >= end_time:
#         end_time = end
#         count += 1

# print(count)