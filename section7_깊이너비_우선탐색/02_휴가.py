import sys
sys.stdin = open("02_input.txt")

# 카운셀러로 일하고 있는 현수는 오늘부터 N+1일째 되는 날 휴가를 가기 위해서, 남은 N일 동안 
# 최대한 많은 상담을 해서 휴가비를 넉넉히 만들어 휴가를 떠나려 한다.
# 현수가 다니는 회사에 하루에 하나씩 서로 다른 사람의 상담이 예약되어 있다.
# 각각의 상담은 상담을 완료하는데 걸리는 날수 T와 상담을 했을 때 받을 수 있는 금액 P로 
# 이루어져 있다.

# 만약 N = 7이고, 아래와 같이 예약이 잡혀 있다면
#   1일  2일  3일  4일  5일  6일  7일
# T  4    2   3    3    2    2    1
# P 20   10   15   20   30   20   10

# 1일에 잡혀있는 상담은 총 4일이 걸리며, 상담했을 때 받을 수 있는 금액은 20이다.
# 만약 1일에 예약된 상담을 하면 4일까지는 상담을 할 수가 없다.
# 하나의 상담이 하루를 넘어가는 경우가 많기 때문에 현수는 예약된 모든 상담을 혼자 할 수 
# 없어 최대 이익이 나는 상담 스케쥴을 짜기로 했다.
# 휴가를 떠나기 전에 할 수 있는 상담의 최대 이익은 1일, 5일, 7일에 있는 상담을 하는 것이며
# 이때의 이익은 20+30+10=60이다.
# 현수가 휴가를 가기 위해 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오

# 모범답안은 times와 prices의 인덱스를 한칸 뒤로 밀어서 "인덱스"를 "날짜"로 보도록 했음.

def DFS(L, price):
    global res
    
    if L >= n:
        if res < price:
            res = price
    else:
        DFS(L + 1, price)    # 상담 안함

        if n - L < times[L]:    # 상담이 휴가날짜를 넘어가는지 확인
            return
    
        DFS(L + times[L], prices[L] + price)    # 상담 함

if __name__ == "__main__":
    n = int(input())
    times = list()
    prices = list()
    res = 0

    for i in range(n):
        t, p = map(int, input().split())
        times.append(t)
        prices.append(p)
    
    DFS(0, 0)
    print(res)
