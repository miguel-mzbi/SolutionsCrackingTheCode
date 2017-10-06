def rotate(matrix):
    N = len(matrix)
    if N == 0 or N == 1:
        return matrix
    top = 0
    left = 0
    right = N-1
    bot = N-1
    while(N >= 2):
        temp = []
        for t in range(left, right, 1):
            temp.append(matrix[top][t])
        lc = left
        for l in range(bot, top, -1):
            matrix[top][lc] = matrix[l][left]
            lc += 1
        for b in range(right, left, -1):
            matrix[b][left] = matrix[bot][b]
        rc = right
        tc = 0
        for r in range(top, bot, 1):
            matrix[bot][rc] = matrix[r][right]
            matrix[r][right] = temp[tc]
            tc += 1
            rc -= 1
        N -= 2
        top +=1
        left +=1
        right -=1
        bot -=1
    return matrix

if __name__ == "__main__":
    
    matrix = [
        [1, 2, 3, 0, 1],
        [4, 5, 6, 0, 1],
        [7, 8, 9, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    rotM = rotate(matrix)
    for row in rotM:
        for col in row:
            print(str(col), end=" ")
        print("")