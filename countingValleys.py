def countingValleys(n, s):
    totalValleys = 0
    status = 0
    for chr in s:

        if chr == 'D':
            status -= 1
        if chr == 'U':
            status += 1
        if status == 0 and chr == 'U':
            totalValleys += 1
        # print status
        prevVal = chr
    # print totalValleys
    return totalValleys


countingValleys(8, 'UDDDUDUU')