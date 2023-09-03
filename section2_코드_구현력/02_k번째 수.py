import sys

sys.stdin = open("02_input.txt", "rt")

# T개의 테스트 케이스가 있다.
# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 
# 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
# input은 한줄씩 읽어온다.

t = int(input())

for i in range(t):
    # 홀수번째 줄
    n, s, e, k = map(int, input().split())
    #print(i, " : ", n, s, e, k)

    # 짝수번째 줄
    num_list = list(map(int, input().split()))
    target_list = num_list[s-1:e]    # list[2:4]라고 하면 3번째부터 4번째 인덱스까지 추출함.
    #print("target :", target_list)
    target_list.sort()  # 변수에 대입하면, 반환값은 none임(주의).

    print("#", i+1, " ", target_list[k-1], sep="")
    # print("#%d %d" %(i+1, target_list[k-1])) 라고 해도 된다. c언어처럼..