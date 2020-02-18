# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    isPossible = True
    for word in note:
        inMaga = magazine.count(word)
        inNote = note.count(word)
        if(inNote>inMaga):
            isPossible = isPossible & False
        else:
            isPossible = isPossible & True
    print('Yes' if isPossible else 'No')

checkMagazine(['hello', 'world'], ['Hello'])