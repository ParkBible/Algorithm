# 아래 2줄은 문제마다 매번 적어준다.
import sys
sys.stdin = open("01_input.txt", "rt")    # rt : read text
n = input()

# 문제 : N의 약수들 중 K번째로 작은 수를 찾고 만약 없으면 -1.

# n_N, n_K = map(int, input().split()) 으로 간단히 매핑해줄 수 있다.
n_N = int(n.split()[0])
n_K = int(n.split()[1])
mylist = []

for i in range(1, n_N+1):     # n_N이 6이면 1~5까지만 돌기 때문에, n_N+1 까지 해줘야 한다.
    if n_N % i == 0:
        mylist.append(i)

#print(mylist)

try:
    print(mylist[n_K-1])
except:
    print(-1)