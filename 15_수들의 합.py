import sys
sys.stdin = open("15_input.txt", "rt")

#N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 
#합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

#이중 for문으로 할수도 있지만, 실행속도가 느리다.
#lt, rt라는 2개의 변수를 잡아서 합인 tot를 구하는 식으로 코드를 짠다. (lt에서부터 rt 바로 전까지의 변수들의 합)

#만약 tot가 m보다 작다면 현재 rt가 가리키는 값을 tot에 더하고, rt를 1 증가시킨다. (rt가 n에 도달했다면 종료)
#tot가 m과 같다면 cnt를 1 증가시키고, tot에서 lt가 가리키는 값을 뺀 후 lt를 1 증가시킨다.
#tot가 m보다 크다면 tot에서 lt가 가리키는 값을 뺀 후 lt를 1 증가시킨다.

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

# res = 0
# cnt = 0
# for idx, x in enumerate(num_list):
#     #idx부터 시작
#     for i in range(idx, len(num_list)):
#         res += num_list[i]
#         if res == m:
#             cnt += 1
#     res = 0

cnt = 0
tot = num_list[0]
lt = 0
rt = 1
while rt <= n :
    if tot < m:
        if rt < n:
            tot += num_list[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= num_list[lt]
        lt += 1
    else:
        tot -= num_list[lt]
        lt += 1
         
print(cnt)