
# Complete the rotLeft function below.
def rotLeft(a, d):


    for x in range(d):
        temp = a[0]
        for y in range(len(a)):
            if(y<len(a)-1):
                a[y] = a[y+1]
        a[-1] = temp
    
    return a



print(rotLeft( [1, 2, 3, 4, 5], 2));