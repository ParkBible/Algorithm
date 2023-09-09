import sys
sys.stdin = open("04_input.txt")

# 유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고 
# 있습니다. 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있
# 으며, 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
# N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 
# 프로그램을 작성하세요.

# 첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
# 두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다.
# 각 승객의 몸무게는 M을 넘지는 않습니다. 즉 탈출을 못하는 경우는 없습니다.

# 실패한 문제
# 그리디는 정렬이 우선임
# 접근방법 : 2명 합했을 때 제일 무거운 조를 우선으로 보내버림
# 2명을 보낸다는 것에 집중하지 말고, 1명만 탈 수 있는지 2명 탈 수 있는지 먼저 판단해야 함.
first_row = list(map(int, input().split()))
num = first_row[0]
weight_limit = first_row[1]
people = list(map(int, input().split()))

# max_weights = []
# result = 0

# while len(people) > 1:
#     for i in range(len(people)):
#         for j in range(i + 1, len(people)):
#             if people[i] + people[j] <= weight_limit and i + j > sum(max_weights) :
#                 max_weights = [people[i], people[j]]
#             elif len(people) == 2:
#                 max_weights = [people[i]]

#     if max_weights == []:
#         break
    
#     for x in max_weights:
#         people.remove(x)

#     max_weights = []
#     result += 1
    
# if len(people) == 1:
#     result += 1

# print(result)

# 모범답안 접근법
# 사람들을 오름차순 정렬한 후, 가장 몸무게가 작은 사람 + 큰 사람을 더해서 안되면 큰 사람 혼자 태워보냄
# 그 후 가장 몸무게가 작은 사람 + 그 다음으로 몸무게가 큰 사람을 더해서 된다면 둘다 태워보냄

people.sort()
result = 0

while people:
    if len(people) == 1:
        result += 1
        break
    if people[0] + people[-1] > weight_limit:
        people.pop()
        result += 1
    else:
        people.pop(0)
        people.pop()
        result += 1

print(result)