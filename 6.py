def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

# Example
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(mat))
