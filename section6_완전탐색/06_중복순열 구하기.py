import sys
sys.stdin = open("06_input.txt")

# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열
# 하는 방법을 모두 출력합니다.

# 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
# 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
# 출력순서는 사전순으로 오름차순으로 출력합니다.

# 뿌리 뻗는 방향을 체크할 때 썼던 ch 리스트를 출력하면 해결되는 문제
# 리스트의 인덱스는 무조건 0부터 시작하도록 하기 (문제에서 1부터 시작된다고 1부터 시작하면 코드 꼬임)

def DFS(L):
    global cnt

    if L == m:
        for i in range(m):
            print(ch[i], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            ch[L] = i
            DFS(L + 1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * m
    cnt = 0

    DFS(0)
    print(cnt)