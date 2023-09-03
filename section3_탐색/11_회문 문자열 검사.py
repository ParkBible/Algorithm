import sys
sys.stdin = open("11_input.txt", "rt")

# N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)
# 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
# 단 회문을 검사할 때 대소문자를 구분하지 않습니다.

# 정말 간단한 방법 : if st == st[::-1]
# 나는 문자열 맞는지 count했는데, 사실 틀린지 비교하고 하나라도 틀린 게 있으면 바로 NO를 출력,
# 무사히 반복문이 종료되었으면 YES 출력하는게 효율적.
# for - else 구문을 이용한다. for문이 if문의 break없이 끝까지 완수되었다면 그 다음에 수행할 동작 입력.
# for ~:
#    if ~:
#       break
# else :


n = int(input())
cnt = 0
for i in range(n):
    st = input()
    if len(st) % 2 == 1:
        length = len(st) - 1
    else:
        length = len(st)

    for j in range(length // 2):

        # st.lower[-1] 이라고 하면 맨 마지막 인덱스가 출력된다. 내가 적은 st.lower[len(st)-1] 과 같은 의미.
        if st.lower()[j] == st.lower()[len(st)-1-j]:    
            cnt += 1
    
    print("#%d" %(i+1), end=' ')
    if cnt >= (length // 2):
        print("YES")
    else:
        print("NO")
    cnt = 0