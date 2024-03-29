import sys
import heapq as hq
sys.stdin = open("11_input.txt")

# 최대힙은 완전이진트리로 구현된 자료구조입니다. 그 구성은 부모 노드값이 왼쪽자식과 오른
# 쪽 자식노드의 값보다 크게 트리를 구성하는 것입니다. 그렇게 하면 트리의 루트(root)노드는 
# 입력된 값들 중 가장 큰 값이 저장되어 있습니다. 예를 들어 5 3 2 1 4 6 7순으로 입력되면 
# 최대힙 트리는 아래와 같이 구성됩니다.
#     7
#  4     6
# 1 3   2 5

# 1) 자연수가 입력되면 최대힙에 입력한다.
# 2) 숫자 0 이 입력되면 최대힙에서 최댓값을 꺼내어 출력한다. 
#  (출력할 자료가 없으면 -1를 출력한다.)
# 3) -1이 입력되면 프로그램 종료한다.

# 풀이는 모범답안과 같다. (부호만 바꾸기)

heap = []

while True:
    n = int(input())

    if n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(-hq.heappop(heap))
    elif n == -1:
        break
    else:
        hq.heappush(heap, -n)
    