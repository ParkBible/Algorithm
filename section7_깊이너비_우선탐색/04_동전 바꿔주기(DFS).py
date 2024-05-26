import sys
sys.stdin = open("04_input.txt")
import copy

# 명보네 동네 가게의 현금 출납기에는 k가지 동전이 각각n1, n2, ... , nk개 씩 들어있다.
# 가게 주인은 명보에게 T원의 지폐를 동전으로 바꿔 주려고 한다. 
# 이때, 동전 교환 방법은 여러 가지가 있을 수 있다. 
# 예를 들어, 10원 짜리, 5원 짜리, 1원 짜리 동전이 각각 2개, 3개, 5개씩 있을 때, 
# 20원 짜리 지폐를 다음과 같은 4가지 방법으로 교환할 수 있다.
#  20 = 10×2
#  20 = 10×1+5×2
#  20 = 10×1+5×1+1×5
#  20 = 5×3+1×5
# 입력으로 지폐의 금액 T, 동전의 가지수 k, 각 동전 하나의금액 pi와 개수 ni가 주어질 때
# (i=1,2,...,k) 
# 지폐를 동전으로 교환하는 방법의 가지 수를 계산하는 프로그램을 작성하시오. 
# 방법의 수는 231을 초과하지 않는 것으로 가정한다. 

# 첫째 줄에는 지폐의 금액 T(0<T≤10,000), 둘째 줄에는 동전의 가지 수 k(0<k≤10), 셋째 줄부터 
# 마지막 줄까지는 각 줄에 동전의 금액 pi(0<pi≤T)와 개수 ni(0<ni≤10)가 주어진다. pi와 ni사이
# 에는 빈 칸이 하나씩 있다.

# 첫 번째 줄에 동전 교환 방법의 가지 수를 출력한다.(교환할 수 없는 경우는 존재하지 않는다.)


# L은 동전의 종류 개수만큼 돌아야 함
# 그 종류당 몇 개만큼 동전을 부여해야 할지 각 루프에서 결정함
# 5원짜리 동전이 3개 있다면 0,1,2,3개 사용하는 경우를 반복함
# L이 어디까지 돌아야 할지(k) 는 거의 정해진 패턴이므로 여기에 맞춰서 생각해보기

# 내가 접근한 방법 : 동전 종류와 개수를 딕셔너리에 저장하고 하나씩 빼는 방법으로 했는데
# 이러면 루프마다 다시 초기화해야되고,, 중복도 제거해줘야되고 여튼 복잡해짐

# def DFS(L, sum):
#     global res
#     global coins
#     print(coins)

#     if L == k:
#         if sum == t:
#             res += 1
#         return

#     for coin in coins:
#         if coins[coin] > 0:
#             coins[coin] -= 1
#             DFS(L + 1, sum + coin)
#             sum = 0
    
# if __name__ == "__main__":
#     t = int(input())
#     k = int(input())
#     coins = dict()
#     res = 0
    
#     for i in range(k):
#         pi, ni = map(int, input().split())
#         coins[pi] = ni

#     coins2 = copy.deepcopy(coins)
    
#     DFS(0, 0)
#     print(res)


def DFS(L, sum):
    global res

    if L == k:    # 이건 거의 고정임
        if sum == t:
            res += 1
        return
    else:
        for i in range(nums[L] + 1):
            DFS(L + 1, sum + prices[L] * i)
    
if __name__ == "__main__":
    t = int(input())
    k = int(input())
    prices = [0] * k
    nums = [0] * k
    res = 0
    
    for i in range(k):
        prices[i], nums[i] = map(int, input().split())
    
    DFS(0, 0)
    print(res)