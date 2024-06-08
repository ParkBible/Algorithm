import sys
sys.stdin = open("06_input.txt")

# 철수와 영희는 서로의 비밀편지를 암호화해서 서로 주고받기로 했다. 
# 그래서 서로 어떻게 암호화를 할 것인지 의논을 하고 있다.
# 영희 : 우리 알파벳 A에는 1로, B에는 2로 이렇게 해서 Z에는 26을 할당하여 번호로 보내기로 하자.
# 철수 : 정말 바보같은 생각이군!! 생각해 봐!! 만약 내가 “BEAN"을 너에게 보낸다면 그것을 암
# 호화하면 25114이잖아!! 그러면 이것을 다시 알파벳으로 복원할 때는 많은 방법이 존재하는데
# 어떻게 할건데... 이것을 알파벳으로 바꾸면 BEAAD, YAAD, YAN, YKD 그리고 BEKD로 
# BEAN말고도 5가지나 더 있군.
# 당신은 위와 같은 영희의 방법으로 암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데 
# 얼마나 많은 방법이 있는지 구하세요.

# 첫 번째 줄에 숫자로 암호화된 코드가 입력된다. (코드는 0으로 시작하지는 않는다, 코드의 길
# 이는 최대 50이다) 0이 입력되면 입력종료를 의미한다.

# 입력된 코드를 알파벳으로 복원하는데 몇 가지의 방법이 있는지 각 경우를 출력한다. 그 가지
# 수도 출력한다. 단어의 출력은 사전순으로 출력한다.

def DFS(L):
    global word

    if L == len(nums):
        res.append(word)
        return
    else:
        if int(nums[L]) != 0:
            if L + 1 < len(nums):
                if int(nums[L + 1]) != 0:
                    add1Digit(L)
            else:
                add1Digit(L)

        if L + 1 < len(nums) and (nums[L + 1] == 0 or int(nums[L] + nums[L + 1]) <= 26):
            if L + 2 < len(nums):
                if int(nums[L + 2]) != 0:
                    add2Digit(L)
            else:
                add2Digit(L)

def add1Digit(L):
    global word

    word += chr(64 + int(nums[L]))
    DFS(L + 1)
    word = word[:-1]   

def add2Digit(L):
    global word

    word += chr(64 + int(nums[L] + nums[L + 1]))
    DFS(L + 2)
    word = word[:-1]
            
if __name__ == "__main__":
    num = input()
    nums = list()
    word = ""
    res = list()

    for s in num:
        nums.append(s)

    DFS(0)

    for r in res:
        print(r)

    print(len(res))