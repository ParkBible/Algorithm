import sys
sys.stdin = open("03_input.txt", "rt")

# 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력
# 하는 프로그램을 작성하세요. (이때 중복은 없앤다.)

n, k = map(int, input().split())
num_list = list(map(int, input().split()))

# res는 list 대신 set이라는 자료구조에 저장한다. 중복을 제거해줌
# append 와 같은 기능인 add를 사용한다.
res_set = set()

# 3장의 카드를 중복 없이 뽑는 알고리즘
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res = num_list[i] + num_list[j] + num_list[m]
            res_set.add(res)

# list의 기능을 쓰기 위해 set을 list로 변환해주기
res_list = list(res_set)
res_list.sort(reverse=True)
print(res_list[k-1])