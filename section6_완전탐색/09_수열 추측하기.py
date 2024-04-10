import sys
sys.stdin = open("09_input.txt")

# 가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있다. 그리고 둘째 줄부터 차례대로 파스칼의 삼각형처럼
# 위의 두개를 더한 값이 저장되게 된다. 예를 들어 N이 4 이고 가장 윗 줄에 3 1 2 4 가 있다고 했을 때, 
# 다음과 같은 삼각형이 그려진다.

# 3 1 2 4
#  4 3 6
#   7 9
#   16

# N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자들을 구하는 프로그램을 작성하시오. 
# 단, 답이 여러가지가 나오는 경우에는 사전순으로 가장 앞에 오는 것을 출력하여야 한다.

# 첫째 줄에 두개의 정수 N(1≤N≤10)과 F가 주어진다. N은 가장 윗줄에 있는 숫자의 개수를 의미하며 
# F는 가장 밑에 줄에 있는 수로 1,000,000 이하이다.


# 8번 문제(순열 구하기)에서부터 시작하여 문제 해결함.
# 
# 모든 경우의 순열에 대해 파스칼의 삼각형 계산 결과와 f가 일치하는지 확인함.
# 파스칼의 삼각형 계산은 DFS2()에서 수행.

triangle_res = 0

def DFS(L):
    if L >= n:
        DFS2(0, res)

        if triangle_res == f:
            for j in res:
                print(j, end=" ")
            sys.exit(0)
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                res[L] = i
                ch[i] = 1
                DFS(L + 1)
                ch[i] = 0

def DFS2(L, nums):
    global triangle_res

    if len(nums) == 1:
        triangle_res = nums[0]
    else:
        new = list()
        for i in range(1, len(nums)):
            new.append(nums[i - 1] + nums[i])
        DFS2(L + 1, new)

if __name__ == "__main__":
    n, f = map(int, input().split())
    ch = [0] * (n + 1)
    res = [0] * n
    
    DFS(0)



# 모범답안
# 사실 파스칼의 삼각형의 꼭대기 계산에는 규칙이 있다.
# 곱셈의 이항계수를 따름
# 1 2 3 즉 n=3인 수열을 파스칼의 삼각형 계산한다고 하면
# n=3일때 1x'1' + 2x'2' + 3x'1' = 6 이라는 것 (1 2 1)
# n=4일때는 1 3 3 1, n=5일 땐 1 4 6 4 1 임
# 이런 이항계수를 구하는 공식은 91번째 라인. 

    
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

if __name__ == "__main__":
    n, f=map(int, input().split())
    p=[0]*n
    b=[1]*n
    ch=[0]*(n+1)
    for i in range(1, n):
        b[i]=b[i-1]*(n-i)//i
    DFS(0, 0)