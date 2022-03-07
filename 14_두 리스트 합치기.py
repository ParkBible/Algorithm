import sys
sys.stdin = open("14_input.txt", "rt")

#오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로
#그램을 작성하세요.
#두 리스트 합친다음에 sort 하면 시간이 nlogn 만큼이 걸리지만, n만큼의 시간만을 쓰는 방법이 있다.

n1 = int(input())
num_list1 = list(map(int, input().split()))
n2 = int(input())
num_list2 = list(map(int, input().split()))

if n1 <= n2:
    n = n1
else:
    n = n2

res_list = []
for i in range(n):
    if num_list1[i] <= num_list2[i]:
        res_list.append(num_list1[i])
        res_list.append(num_list2[i])
    else:
        res_list.append(num_list2[i])
        res_list.append(num_list1[i])


if n1 == n:
    res_list += num_list2[n:]
else:
    res_list += num_list1[n:]

print(res_list)