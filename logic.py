import random


def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    return mat


def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2


def compress(mat):
    newmat = []
    for i in range(4):
        newmat.append([0] * 4)
    change = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                newmat[i][pos] = mat[i][j]
                if pos!=j:
                    changed=True
                pos += 1
    return newmat, change


def merge(mat):
    change = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = 2 * mat[i][j]
                mat[i][j + 1] = 0
                change = True
    return mat, change


def reverse(mat):
    newmat = []
    for i in range(4):
        newmat.append([])
        for j in range(4):
            newmat[i].append(mat[i][4 - j - 1])
    return newmat


def transpose(mat):
    newmat = []
    for i in range(4):
        newmat.append([])
        for j in range(4):
            newmat[i].append(mat[j][i])
    return newmat


def get_curr_state(mat):
    # anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    # anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    # Every row and column except last
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] or mat[i][j] == mat[i + 1][j]:
                return 'GAME NOT OVER'
    # checking for last row and column
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER'
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'
    return 'LOST'


def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    for i in range(4):
        for j in range(4):
            if grid[i][j]!=new_grid[i][j]:
                changed=True
    return new_grid, changed


def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed1 = compress(new_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    new_grid = reverse(new_grid)
    for i in range(4):
        for j in range(4):
            if grid[i][j]!=new_grid[i][j]:
                changed=True
    return new_grid, changed


def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed1 = compress(new_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    new_grid = transpose(new_grid)
    for i in range(4):
        for j in range(4):
            if grid[i][j]!=new_grid[i][j]:
                changed=True
    return new_grid, changed


def move_down(grid):
    new_grid = transpose(grid)
    new_grid = reverse(new_grid)
    new_grid, changed1 = compress(new_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    new_grid = reverse(new_grid)
    new_grid = transpose(new_grid)
    for i in range(4):
        for j in range(4):
            if grid[i][j]!=new_grid[i][j]:
                changed=True
    return new_grid, changed

def print_matrix(mat):
    for i in range(4):
        for j in range(4):
            print(mat[i][j],end=" ")
        print()
    print()
