def jumpingOnClouds(c):
    step = 0
    count = 0
    for i in range(len(c)):
        if i>= count and len(c)-3>= i :
            if c[i+1] == 1:
                count = count+2
            if c[i+1] == 0 and c[ i + 2] == 0:
                count = count+2
            if c[i+1] == 0 and c[i+2] == 1:
                count = count +1
            step += 1
        elif len(c)-1:
            step += 1

    print(step)
    return step




jumpingOnClouds([0, 0, 0, 0, 1, 0])