import sys
sys.stdin = open("09_input.txt")

# 두 문자열의 알파벳 나열 순서가 다르지만 그 구성이 일치하면 두 단어는 아나그램(Anagram)이라고 합니다. 
# 예를 들면 AbaAeCe 와 baeeACA 는 알파벳 나열 순서는 다르지만 그 구성을 살펴보면 
# A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다. 
# 즉 어느 한 단어를 재배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
# 길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세요. 판별시 대소문자가 구분됩니다.

# 첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다. 
# 두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.


# 딕셔너리의 특징은, 리스트와 달리 인덱스(숫자)값이 아닌 키(문자)값으로도 접근 가능하다는 것. dict1["문자(key)"] = value
# 다만 딕셔너리는 key가 중복일 수 없다.

# 직관적으로는 for문 돌면서 if - in 을 사용하면 된다...

w1 = input()
w2 = input()
li1 = list(w1)
li2 = list(w2)

for i in range(len(w1)):
    if w1[i] in li2:
        li1.remove(w1[i])
        li2.remove(w1[i])

if len(li1) == 0 and len(li2) == 0:
    print("YES")
else:
    print("NO")


# 모범답안
# w1의 요소를 딕셔너리의 key로 한 후 그 키의 value를 "개수"로 한다.
# sH.get(x, 0)은 해당 키가 없으면 0, 있으면 그 키의 value를 리턴한다. 즉 거기다 +1을 하면 개수가 카운팅되는 것.
# w2에 그 값이 있다면 카운팅한 value를 도로 빼서 0으로 만든다.

# w1 = input()
# w2 = input()
# sH = dict()
# for x in w1:
#     sH[x] = sH.get(x, 0) + 1

# for x in w2:
#     sH[x] = sH.get(x, 0) - 1

# for x in w1:
#     if sH.get(x) > 0:
#         print("NO")
#         break
# else:
#     print("YES")