import sys
sys.stdin = open("04_input.txt", "rt")

# N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
# N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
# 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
# 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

# 반올림할때는 round를 쓰는 대신 +0.5를 한 다음 int로 변형하는 방법을 사용합니다.
# round는 round_half_even 방식 : 2.5를 2로 반올림하기 때문(경계선에 있으면 짝수가 되는 쪽으로 반올림함).

n = int(input())
score_list = list(map(int, input().split()))
#print(score_list)

avg = int(sum(score_list) / n + 0.5)

# 비교는 절댓값(abs_list)으로 하되, 동일한 값과 마주치면 원래 값(dif_list)로 비교하여 더 높은 쪽의 인덱스 번호 선택.
# > 로 비교하기 때문에, 학생번호가 빠른 학생의 번호가 선택된다.

# 모범답안에서는 리스트 2개 만드는 대신 변수를 3개 만들었다. (절댓값, 원래값, 인덱스번호)

dif_list = []
abs_list = []
for i in score_list:
    dif_list.append(i - avg)
    abs_list.append(abs(i - avg))

arr_min = float("inf")
min_idx = 0

# for idx, x in enumerate(dif_list): 으로 하면 인덱스값과 값 모두 가져올 수 있다.
for i in range(n):
    if arr_min > abs_list[i]:
        arr_min = abs_list[i]
        min_idx = i
    elif arr_min == abs_list[i]:
        if dif_list[min_idx] < dif_list[i]:
            arr_min = abs_list[i]
            min_idx = i

print(avg, min_idx + 1)
