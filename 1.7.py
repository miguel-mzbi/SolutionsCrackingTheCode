def zeros(matrix, m, n):
    if m == 0 or n == 0:
        return matrix
    if m == 1 and n == 1:
        return matrix
    rows = []
    cols = []
    for j in range(m):
        for i in range(n):
            if matrix[j][i] == 0:
                rows.append(j)
                cols.append(i)

    for h in rows:
        for i in range(n):
            matrix[h][i] = 0
    for k in cols:
        for l in range(m):
            matrix[l][k] = 0
    return matrix

if __name__ == "__main__":
    
    matrix = [
        [1, 2, 3, 0, 1],
        [4, 5, 6, 8, 1],
        [7, 8, 9, 0, 1],
        [0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    zerM = zeros(matrix, 5, 5)
    for row in zerM:
        for col in row:
            print(str(col), end=" ")
        print("")