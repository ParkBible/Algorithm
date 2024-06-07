import sys
sys.stdin = open("05_input.txt")

# N개의 동전을 A, B, C 세명에게 나누어 주려고 합니다.
# 세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 총액이 가장 큰 
# 사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.
# 단 세 사람의 총액은 서로 달라야 합니다.

# 첫째 줄에는 동전의 개수 N(3<=N<=12)이 주어집니다.
# 그 다음 N줄에 걸쳐 각 동전의 금액이 주어집니다.
# 총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력하세요.

# 29(12+17), 32(8+9+15), 34(11+23) 로 분배하면 최대금액과 최소금액의 차가 5가 되어
# 5가 최소차가 된다.

def DFS(L):    # 동전의 개수만큼 L을 돌기로 한다.
    global res

    if L == n:
        if sum(prices) == sum(coins) and max(prices) - min(prices) < res and len(set(prices)) == len(prices):
            res = max(prices) - min(prices)
        # prices = [0] * 3
        return
    else:
        for i in range(len(prices)):
            prices[i] += coins[L]
            DFS(L + 1)
            prices[i] -= coins[L]    # 중요!!! 옆 가지로 가기 위해(즉, 해당 동전 L을 다른 사람에게 주기 위해) i에게 줬던 것을 취소시키고 이전 레벨로 올라가야 함
                                     # 왜? 이번 문제는 sum이라는 파라미터가 DFS에 없기 때문.
                                     # 원래 sum에 더하거나 / 더하지 않거나 하는 식으로 했지만 이번 문제는 global한 리스트 변수인 prices에 기록함
if __name__ == "__main__":
    n = int(input())
    res = 99999999
    prices = [0] * 3
    coins = list()

    for i in range(n):
        coins.append(int(input()))

    DFS(0)
    print(res)