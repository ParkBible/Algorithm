import sys
sys.stdin = open("01_input.txt")

# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용해서 출력해야 합니다.

def DFS(num):
    if num > 1:
        DFS(num // 2)
        print(num % 2)
    elif num == 1:
        print(num)

if __name__=="__main__":
    n = int(input())
    DFS(n)


# 모범답안
# def DFS(x):
#     if x == 0:
#         return
#     else:
#         DFS(x // 2)
#         print(x % 2)