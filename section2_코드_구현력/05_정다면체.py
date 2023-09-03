import sys
sys.stdin = open("05_input.txt", "rt")

# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
# 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

n, m = map(int, input().split())
sum_list = [0] * (n+m+1)

# 두 주사위의 합(특정 값)이 몇 번 나왔는지 리스트 생성
for i in range(1, n+1):
    for j in range(1, m+1):
        sum = i + j
        sum_list[sum] += 1

# 최대 횟수 구함
max_cnt = 0
for i in sum_list:
    if max_cnt < i:
        max_cnt = i

# 최대 횟수로 나온 값들 출력
res_list = []
for idx, x in enumerate(sum_list):
    if x == max_cnt:
        print(idx, end=' ')    # 옆으로 쭉 출력할땐 이렇게!
