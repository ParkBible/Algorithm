import sys
sys.stdin = open("03_input.txt")

# 무게가 서로 다른 K개의 추와 빈 그릇이 있다. 모든 추의 무게는 정수이고, 
# 그릇의 무게는 0으로 간주한다. 양팔저울을 한 번만 이용하여 원하는 물의 무게를 그릇에 담고자 한다.
# 주어진 모든 추 무게의 합을 S라 하자. 예를 들어, 추가 3개이고, 각 추의 무게가 {1, 2, 6}이
# 면, S=9이고, 양팔저울을 한 번만 이용하여 1부터 S사이에 대응되는 모든 무게의 물을 다음과 
# 같이 그릇에 담을 수 있다. X는 그릇에 담는 물의 무게이고, ⎕은 그릇을 나타낸다.

# X     1     2     3       4         5         6       7       8       9
#      ⎕:1 ⎕:2 ⎕:(1+2) (⎕+2):6  (⎕+1):6   ⎕:6   ⎕:(1+6) ⎕:(2+6) ⎕:(1+2+6)

# 만약 추의 무게가 {1, 5, 7}이면 S=13이고,
# 그릇에 담을 수 있는 물의 무게는 {1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13}이고,
# 1부터 S사이에서 무게에서 9와 10에 대응하는 무게의 물을 담을 수 없다. 
# K(3<=K<=13)개의 추 무게가 주어지면, 1부터 S사이의 정수 중 측정이 불가능한 물의 무게는 
# 몇 가지가 있는 지 출력하는 프로그램을 작성하세요

# 첫 번째 줄에 자연수 K(3<=K<=13)이 주어집니다.
# 두 번째 줄에 K개의 각 추의 무게가 공백을 사이에 두고 주어집니다. 각 추의 무게는 1부터 
# 200,000까지이다.
# 첫 번째 측정이 불가능한 가지수를 출력하세요.

# 나올 수 있는 경우를 담은 리스트를 만들어 놓고 하나씩 제하는 방식
# s가 너무 크면 시간이 상당히 오래 걸림
def DFS(L, total):
    if L == k or total > s:
        if total in nums:
            nums.remove(total)
    else:
        DFS(L + 1, total + li[L])
        DFS(L + 1, total - li[L])
        DFS(L + 1, total)

if __name__ == "__main__":
    k = int(input())
    li = list(map(int, input().split()))
    s = sum(li)

    nums = [i + 1 for i in range(s)]
    
    DFS(0, 0)
    print(len(nums))


# 모범답안. 중복을 피하기 위해 set 자료형을 사용함
def DFS(L, total):
    if L == k:
        if 0 < total <= s:
            res.add(total)
    else:
        DFS(L + 1, total + li[L])
        DFS(L + 1, total - li[L])
        DFS(L + 1, total)

if __name__ == "__main__":
    k = int(input())
    li = list(map(int, input().split()))
    s = sum(li)

    nums = [i + 1 for i in range(s)]
    res = set()
    
    DFS(0, 0)
    print(s - len(res))