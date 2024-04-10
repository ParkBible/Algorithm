import sys
sys.stdin = open("08_input.txt")

# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
# 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

# 어려웠던 문제,,,
# 체크 리스트를 "인덱스"로 확인하여 리스트의 값이 0이면 결과에 포함, 1이면 포함시키지 않는다. (중복된 번호를 뽑지 않기 위해)
# 끝까지 다 뻗은 뒤 올라올 때는 리스트의 값을 0으로 초기화 시킨다.

# L은 트리의 현재 레벨이란 점을 기억하기..

def DFS(L):
    global cnt

    if L == m:
        for j in range(L):
            print(res[j], end=" ")   
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                res[L] = i    # 레벨마다 숫자를 하나씩 선택
                ch[i] = 1    # 건너뛰게 하기 위함
                DFS(L + 1)    # 다음 레벨로 넘어감
                ch[i] = 0    # 리스트 값 초기화시킴
                
if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * (n + 1)
    res = [0] * n
    cnt = 0

    DFS(0)
    print(cnt)