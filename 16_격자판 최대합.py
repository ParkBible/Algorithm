import sys
sys.stdin = open("16_input.txt", "rt")

# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력합니다.

n = int(input())
l = []

for i in range(n):
    temp = list(map(int, input().split()))
    l.append(temp)

print(l)