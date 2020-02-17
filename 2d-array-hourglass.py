# Complete the hourglassSum function below.
def hourglassSum(arr):
    largestSum = 0
    sums = []
    for x in range(4):
        for y in range(4):
            # loop in the hourglass:
            sum = 0
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if i == x + 1 and (j == y + 2 or j == y):
                        print(arr[i][j])
                        continue
                    sum = sum + arr[i][j]
                    sums.append(sum)
            # print(sum)
            print('---------')
            largestSum = largestSum or sum
            largestSum = sum if sum > largestSum else largestSum
            
    return largestSum


print(
    hourglassSum(
        [
            [-9, -9, -9, 1, 1, 1],
            [0, -9, 0, 4, 3, 2],
            [-9, -9, -9, 1, 2, 3],
            [0, 0, 8, 6, 6, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, 1, 2, 4, 0],
        ]
    )
)
