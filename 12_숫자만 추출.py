import sys
sys.stdin = open("12_input.txt", "rt")

# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만
# 듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다

inp = input()
dec = ""

for idx, i in enumerate(inp):
    if i.isdecimal():    # i.isdigit() : 2의3승 같은것도 인식
        dec += i

dec = int(dec)
print(dec)

cnt = 0
for i in range(1, dec+1):
    if dec % i == 0:
        cnt += 1

print(cnt)