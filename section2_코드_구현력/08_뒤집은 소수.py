import sys
sys.stdin = open("08_input.txt", "rt")

# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 
# 프로그램을 작성하세요. 단 910를 뒤집으면 19로 숫자화 해야 한다.
# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시
# 작성하여 프로그래밍 한다.

n = int(input())
num_list = list(map(int, input().split()))
rev_list = []

def reverse(x):
    x = str(x)
    rev = ""
    for i in range(len(x)):
        rev += x[len(x)-1-i]    # i 찍어보고 결과론적으로 인덱스 바꾼것
    return int(rev)

for i in num_list:
    rev_list.append(reverse(i))
#print(rev_list)

# x%i가 0이라는 조건을 만족한다면 return False로 바로 반복문을 종료해 버리는 것이 효율적이다.
# 반복문이 도중에 return False 되지 않고 정상적으로 종료되었다면 return True를 해준다.
def isPrime(x):
    prime = 0
    for i in range(2, x):
        if x%i == 0:
            prime = 1
    if(prime == 0) and (x != 1):    # 1은 소수가 아니므로 따로 처리해줘야 한다.
        print(x, end=" ")

for i in rev_list:
    isPrime(i)

