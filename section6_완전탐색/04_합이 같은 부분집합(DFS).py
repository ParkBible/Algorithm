import sys
sys.stdin = open("04_input.txt")

# N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때 
# 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고, 그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.
# 둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어야 합니다.
# 예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10} 으로 두 부분집합의 합이 
# 16으로 같은 경우가 존재하는 것을 알 수 있다.

# 첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
# 두 번째 줄에 집합의 원소 N개가 주어진다. 각 원소는 중복되지 않는다.


# 접근 방법: 왼쪽, 오른쪽 집합을 만든다. 그리고 요소들의 인덱스를 main의 for문 안에 하나씩 넣은 뒤 
# 그 인덱스에 해당하는 숫자가 포함된 집합이면 왼쪽, 아니라면 오른쪽으로 뻗어 나감.

# ??: 조건에 맞는 집합이 도출되었을 때 바로 return 하는 방법을 모르겠다. 
# 그래서 결과가 나왔든 나오지 않았든 끝까지 다 돌고(비효율적) global 변수를 정의하여 사용하였다.

def DFS(idx):
    left = []
    right = []
    global res

    if idx > n - 1:
        for i in range(0, n):
            if ch[i] == 0:
                left.append(nums[i])
            else:
                right.append(nums[i])

        if len(left) != 0 and len(right) != 0:
            if sum(left) == sum(right):
                res = True

    else:
        ch[idx] = 0
        DFS(idx + 1)
        ch[idx] = 1
        DFS(idx + 1)

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    ch = [0] * (n + 1)
    res = False

    for i in range(n):
        DFS(i)
    
    if res:
        print("YES")
    else:
        print("NO")


# 모범답안
        
# L: 리스트 a의 인덱스, sum: 누적값.
# 굳이 집합의 원소를 모두 비교할 필요 없이, 두 집합 각각의 "합계" 만을 비교해도 무방한 문제였다.
        
def DFS(L, sum):
    if sum>total//2:    # 시간 복잡도를 줄이기 위해, sum이 전체 합계의 절반을 넘으면 뿌리를 끝까지 내리지 않고 바로 컷
        return
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)    # 프로그램을 바로 종료시키는 코드
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
    print("NO")