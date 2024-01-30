import sys
sys.stdin = open("07_input.txt")

# 다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환
# 해주려면 어떻게 주면 되는가? 각 단위의 동전은 무한정 쓸 수 있다.

# 첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 두 번째 줄에는 N개의 동전의 종류가 
# 주어지고, 그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다. 
# 각 동전의 종류는 100원을 넘지 않는다.

# 첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.


# 재귀함수 돌기 전 앞전에 끊는 조건을 생각하기, 그리고 시간을 줄이기 위해 주어진 데이터의 정렬도 고려하기

def DFS(idx):
    global min

    if sum(ch) > m:
        return
    
    if idx > min:
        return

    if sum(ch) == m:
        if idx < min:    # idx 대신 len(ch)를 써서 4, 5번 답안에서 무한루프(ch의 길이는 고정돼있잖아,,)
            min = idx
    else:
        for type in types:
            ch[idx] = type
            DFS(idx + 1)

if __name__ == "__main__":
    n = int(input())
    types = list(map(int, input().split()))
    m = int(input())
    ch = [0] * n
    min = 9999999
    types.sort(reverse=True)    # 큰 동전부터 시작하는게 이득이라 내림차순 정렬

    DFS(0)
    print(min)