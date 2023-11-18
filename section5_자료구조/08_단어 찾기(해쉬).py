import sys
sys.stdin = open("08_input.txt")

# 현수는 영어로 시를 쓰는 것을 좋아합니다.
# 현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다. 
# 이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다.
# 여러분이 찾아 주세요.

# 첫 번째 줄에 자연수 N(3<=N<=100)이 주어진다.
# 두 번째 줄부터 노트에 미리 적어놓은 N개의 단어가 주어지고, 이어 바로 다음 줄부터 시에 
# 쓰인 N-1개의 단어가 주어진다.

# 첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.

n = int(input())
note_words = []
poem_words = []

for i in range(n):
    note_words.append(input())

for i in range(n - 1):
    poem_words.append(input())

for word in note_words:
    if word not in poem_words:
        print(word)


# 모범답안
# 리스트를 굳이 2개 만들 필요 없이, 딕셔너리로 해결할 수 있음.
# 시에 적힌 단어들을 키값으로 설정하고, value를 모두 1로 한 다음 노트에 적힌 단어들의 value를 모두 0으로 한다.
# 그럼 value가 1인 단어가 하나 남을 것이다. 그 값의 key가 정답.

# n = int(input())
# words = dict()

# for i in range(n):
#     word = input()
#     words[word] = 1

# for i in range(n):
#     word = input()
#     words[word] = 0

# for key, val in words:
#     if val == 1:
#         print(key)
#         break