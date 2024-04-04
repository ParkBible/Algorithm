import sys
sys.stdin = open("01_input.txt")

# 이번 정보올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를 
# 풀려고 합니다. 각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩
# 니다. 제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다. (해당문제는 
# 해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있습니다.)

# 첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다. 
# 두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.

# 부분집합을 전체 순회하는 문제

def DFS(L, sum, time):
    global res

    if time > m:
        return

    if L == n:
        if res > sum:
            res = sum
    else:
        DFS(L + 1, sum + scores[L], time + times[L])    # 문제 푸는 경우
        DFS(L + 1, sum, time)    # 문제 안 푸는 경우

if __name__ == "__main__":
    n, m = map(int, input().split())
    scores = list()
    times = list()
    res = -1

    for i in range(n):
        score, time = map(int, input().split())
        scores.append(score)
        times.append(time)

    DFS(0, 0, 0)
    print(res)