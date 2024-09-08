
### PART 1

print("PART 1\n")

def my_matrix(n):
    matrix = [[0] * n for _ in range(n)]

    x = (n - 1) // 2
    y = (n - 1) // 2
    num = 1

    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    indexOfDirect = 0

    step = 1
    i = 0

    while num <= n ** 2:
        while 1:
            for j in range(step):
                if (0 <= x and x < n) and (0 <= y and y < n):
                    matrix[x][y] = num
                    num = num + 1

                direction = direct[indexOfDirect]

                x_direct = direction[0]
                y_direct = direction[1]

                x = x + x_direct
                y = y + y_direct

            if indexOfDirect == 3:
                indexOfDirect = 0
            else:
                indexOfDirect += 1

            i = i + 1

            if i == 2:
                i = 0
                break

        step += 1

    return matrix


n = int(input("Size of the square matrix: "))
while n < 0:
    print('must be non-negative')
    n = int(input())

matrix = my_matrix(n)
for row in matrix:
    print(' '.join(f'{num:2}' for num in row))

### PART 2

print("\nPART 2")

def sumOfDiagonals(matrix):
    primarySum = 0
    secondarySum = 0

    for i in range(n):
        primarySum += matrix[i][i]
        secondarySum += matrix[i][n - i - 1]

    return primarySum, secondarySum