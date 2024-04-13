import sys
sys.stdin = open("10_input.txt")

# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑는 방법의 수를 출력하는
# 프로그램을 작성하세요.

# 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
# 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
# 출력순서는 사전순으로 오름차순으로 출력합니다.

def DFS(L):
    if L >= m:
        if sorted(res) not in sav:
            sav.append(sorted(res))

            for i in res:
                print(i, end=" ")
            print()
            
    else:
        for j in range(1, n + 1):
            if ch[j] == 0:
                res[L] = j
                ch[j] = 1
                DFS(L + 1)
                ch[j] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * (n + 1)
    res = [0] * m
    sav = list()

    DFS(0)
    print(len(sav))


# 모범답안
# 

# def DFS(L, s):
#     global cnt
#     if L==m:
#         for i in range(m):
#             print(res[i], end=' ')
#         print()
#         cnt+=1
#     else:
#         for i in range(s, n+1):
#             res[L]=i
#             DFS(L+1, i+1)
           

# n, m=map(int, input().split())
# res=[0]*(n+1)
# cnt=0
# DFS(0, 1)
# print(cnt)