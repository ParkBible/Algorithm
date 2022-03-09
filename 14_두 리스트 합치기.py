import sys
sys.stdin = open("14_input.txt", "rt")

#★★★★★★실수다발문제★★★★★★
#오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로
#그램을 작성하세요.
#두 리스트 합친다음에 sort 하면 시간이 nlogn 만큼이 걸리지만, n만큼의 시간만을 쓰는 방법이 있다.
#num_list1의 인덱스를 가리키는 포인터 p1, num_list2의 인덱스를 가리키는 포인터 p2를 만들고, p1,p2를 비교한 뒤 작은쪽을 +1한다.
#while문을 사용하는 예제. (변수가 2개)

n1 = int(input())
num_list1 = list(map(int, input().split()))
n2 = int(input())
num_list2 = list(map(int, input().split()))

p1 = 0
p2 = 0
res_list = []
while p1<n1 and p2<n2:
    if num_list1[p1] <= num_list2[p2]:
        res_list.append(num_list1[p1])
        p1 += 1
    else:
        res_list.append(num_list2[p2])
        p2 += 1

# 어떤 포인터가 끝까지 못갔는지 찾기. (p1<=n1이 참이면 밑에조건이 실행되지 않기 때문에 elif로 하면 안된다.)
if p1<=n1:
    res_list += num_list1[p1:]
if p2<=n2:
    res_list += num_list2[p2:]

for i in res_list:
    print(i, end=" ")