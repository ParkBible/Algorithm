import sys
#sys.stdin = open("16_input.txt", "rt")

# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력합니다.

n = int(input())
board = []

for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)

max = 0
sum_of_left = 0
sum_of_right = 0

for i, row in enumerate(board):
    max_dict = {"row": 0, "column": 0, "left_diagonal": 0, "right_diagonal": 0}

    # for문 안에서 sum_of_row += board[i][j] 하는것과 같음
    sum_of_row = sum(row)
    sum_of_column = 0

    if sum_of_row > max:
        max = sum_of_row

    for j in range(len(board)):
        sum_of_column += board[j][i]
    
    if sum_of_column > max:
        max = sum_of_column

    sum_of_left += board[i][i]
    sum_of_right += board[i][len(board) - 1 - i]

    if sum_of_left > max:
        max = sum_of_left

    if sum_of_right > max:
        max = sum_of_right

print(max)