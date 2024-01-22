import sys
sys.stdin = open("05_input.txt")

# 철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태
# 울수가 없다. 철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
# N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 
# 무게를 구하는 프로그램을 작성하세요.

# 첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다.
# 둘째 줄부터 N마리 바둑이의 무게가 주어진다.

# 4번과 비슷한 문제 같지만 그대로 하면 time limit을 초과하므로, sum > c 외에도 중간에 끊을 조건을 하나 더 추가해주어야 함.
# 만약 지금까지 만든 부분집합의 합 + (앞으로 판단해야 할 부분집합 바둑이들의 값) 이 max보다 작다면 return한다.
# (앞으로 판단해야 할 부분집합 바둑이들의 값) = 바둑이 전체 무게 총합 - 지금까지 판단한(sum에 누적되지 않은 것들도 포함) 바둑이들의 누적값

# 지금까지 판단한 바둑이들의 누적값을 기록할 변수, tsum을 만든다.

def DFS(idx, sum, tsum):
    global max

    if sum + (total - tsum) < max:
        return

    if sum > c:
        return

    if idx == n:
        if max < sum:
            max = sum
    else:
        DFS(idx + 1, sum + w[idx], tsum + w[idx])
        DFS(idx + 1, sum, tsum + w[idx])

if __name__ == "__main__":
    c, n = map(int, input().split())
    w = []
    max = 0

    for i in range(n):
        w.append(int(input()))

    total = sum(w)    # 바둑이 전체 무게 총합
    
    DFS(0, 0, 0)
    print(max)