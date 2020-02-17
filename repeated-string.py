# THE BAD STYLE

# def repeatedString(s, n):
#     counter  = 0
#     finalString = []
#     for x in range(n):
#         finalString.append(s[x%len(s)])
#     # print(finalString)
#     for x in finalString:
#         if x == 'a':
#             counter += 1
#     print(counter)
#     return counter

# repeatedString('aba', 10)

#THE GOOD STYLE

def repeatedString(s, n):
    result = divmod(n, len(s))
    repeats = result[0]
    remainder = result[1]

    aInString = s.count('a')
    aInSubstring = s[:remainder].count('a')
    return aInString*repeats+aInSubstring

    

print(repeatedString('aba', 100000000000))