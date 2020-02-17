
# Complete the minimumBribes function below.
def minimumBribes(q):
    totalMoves = 0
    
    q = [p-1 for p in q]

    for i, num in enumerate(q):

        if num-i > 2:
            print('Too chaotic')
            return
        
        for y in range(max(num-1, 0),i):
            if q[y]> q[i]:
                totalMoves += 1

    print(totalMoves)


minimumBribes([2, 1, 5, 3, 4])
minimumBribes([2, 5, 1, 3, 4])