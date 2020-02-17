def jumpingOnClouds(c):
    steps = 0
    x = 0
    while(x<len(c)-2):
        if c[x+1] == 0 and c[x+2] == 0:
            x += 2
        elif c[x+1] == 0 and c[x+2] == 1:
            x += 1
        elif c[x+1] == 1 and c[x+2] == 0:
            x += 2
        else:
            x =+1
        
        steps = steps+1
        
    if c[-1] == 0 and x == len(c)-2: steps += 1
    print(steps)
    return steps




jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])