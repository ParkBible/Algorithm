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