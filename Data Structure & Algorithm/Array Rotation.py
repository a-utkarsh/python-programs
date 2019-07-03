#Python3 program to rotate a matrix by 90 degrees
N = 4


# An Inplace function to rotate
# N x N matrix by 90 degrees in
# anti-clockwise direction
def displayMatrix(mat):
    for i in range(0, N):

        for j in range(0, N):
            print(mat[i][j], end=' ')
        print("")

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
displayMatrix(mat)

print("")

def rotateMatrix(mat):
    # Consider all squares one by one
    for i in range(0, int(N / 2)):

        # Consider elements in group
        # of 4 in current square
        for j in range(i, N - i - 1):
            # store current cell in temp variable
            temp = mat[i][j]

            # move values from right to top
            mat[i][j] = mat[j][N - 1 - i]
            #displayMatrix(mat)
            #print()

            # move values from bottom to right
            mat[j][N - 1 - i] = mat[N - 1 - i][N - 1 - j]
            #displayMatrix(mat)
            #print()
            # move values from left to bottom
            mat[N - 1 - i][N - 1 - j] = mat[N - 1 - j][i]
            #displayMatrix(mat)
            #print()
            # assign temp to left

            mat[N - 1 - j][i] = temp
            #displayMatrix(mat)
            #print()

# Function to pr the matrix



# Driver Code
#mat = [[0 for x in range(N)] for y in range(N)]

# Test case 1


'''
# Test case 2
mat = [ [1, 2, 3 ],
        [4, 5, 6 ],
        [7, 8, 9 ] ]

# Test case 3
mat = [ [1, 2 ],
        [4, 5 ] ]

'''

rotateMatrix(mat)

# Print rotated matrix
displayMatrix(mat)
