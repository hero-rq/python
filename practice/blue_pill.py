'''
The question
Among the children's toys sold by Starlink, the most popular product is Bead Escape. Ball escape is a game in which red beads and blue beads are put one by one on a rectangular board, and then red beads are pulled out through a hole.
The vertical size of the board is N and the horizontal size is M, and for convenience, it is divided into 1×1 compartments. The outermost rows and columns are all blocked, and the board has a hole. The size of the red and blue beads is the size that fills the 1×1 compartment on the board, and each has one. The goal of the game is to pull out the red beads through the hole. At this time, blue beads should not enter the hole.
At this time, you can't touch the bead with your hands, but you have to roll it here and there using gravity. There are four possible movements: tilting to the left, tilting to the right, tilting to the up, and tilting to the down.
In each movement, the ball moves simultaneously. If the red bead falls into the hole, it is a success, but if the blue bead falls into the hole, it is a failure. Even if the red and blue beads fall into the hole at the same time, it is a failure. Red and blue beads cannot be in the same compartment at the same time. Also, the size of the red and blue beads takes up one space. Stop tilting until the beads are no longer moving.
Given the state of the board, write a program to determine at least how many times the red bead can be pulled through the hole.

Input
In the first line, two integers N, M (3≤N, M≤10) are given, meaning the vertical and horizontal size of the board. The following N lines are given a string of length M indicating the shape of the board. The string consists of '.', '#', 'O', 'R', and 'B'. '.' means blank, '#' means an obstacle or wall in which the ball cannot move, and 'O' means the position of the hole. 'R' is the location of the red bead and 'B' is the location of the blue bead.
All input boards have a '#' on the edge. The number of holes is one, and red and blue beads are always given one.

Output
Print out at least how many times the red bead can be pulled out through the hole. If the red bead cannot be pulled out through the hole by moving less than 10 times, output -1.
'''

def move_bead(board, red_x, red_y, blue_x, blue_y, moves):
    if board[red_x][red_y] == 'O':
        return moves
    if board[blue_x][blue_y] == 'O':
        return -1

    min_moves = float('inf')  # Initialize the minimum number of moves to infinity

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = red_x + dx, red_y + dy
        if board[nx][ny] != '#':
            red_x, red_y = nx, ny
        nx, ny = blue_x + dx, blue_y + dy
        if board[nx][ny] != '#':
            blue_x, blue_y = nx, ny
        board[red_x][red_y] = 'R'
        board[blue_x][blue_y] = 'B'
        min_moves = min(min_moves, move_bead(board, red_x, red_y, blue_x, blue_y, moves + 1))
        board[red_x][red_y] = '.'
        board[blue_x][blue_y] = '.'

    return min_moves

n, m = map(int, input().split())
board = []
red_x, red_y = None, None
blue_x, blue_y = None, None
for i in range(n):
    row = input()
    if 'R' in row:
        red_x, red_y = i, row.index('R')
    if 'B' in row:
        blue_x, blue_y = i, row.index('B')
