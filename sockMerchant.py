def sockMerchant(n, ar):
    uniqueArr = []

    count = 0
    for x in ar:
        if count == ar.index(x):
            uniqueArr.append(x)
        count += 1

    pairCount = 0
    pairCount
    for x in uniqueArr:
        freq = 0
        for y in ar :
            if x==y:
                freq = freq+1
        print(freq)
        pairCount = pairCount + int(freq/2)
    return pairCount



sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10 ,20])