import sys
sys.stdin = open("11_input.txt", "rt")

# N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)
# 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
# 단 회문을 검사할 때 대소문자를 구분하지 않습니다.

n = int(input())
cnt = 0
for i in range(n):
    st = input()
    if len(st) % 2 == 1:
        length = len(st) - 1
    else:
        length = len(st)

    for j in range(length // 2):
        if st.lower()[j] == st.lower()[len(st)-1-j]:
            cnt += 1
    #print(cnt)
    print("#%d" %(i+1), end=' ')
    if cnt >= (length // 2):
        print("YES")
    else:
        print("NO")
    cnt = 0