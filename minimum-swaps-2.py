# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    minVal = min(arr)
    for x in range(len(arr)-1):
        
        #swap the min value to it's original position
        
        if minVal != arr[x]:
            swaps += 1
        tempVal = arr[x]
        arr[arr.index(minVal)] = tempVal
        arr[x] = minVal
        minVal += 1

    # print(arr)
    return swaps



print(minimumSwaps([2, 3, 4, 1, 5]))
print(minimumSwaps([4, 3,1, 2]))
print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))