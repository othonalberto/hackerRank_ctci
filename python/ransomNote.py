def generateDicts(magazine, ransom):
    dict1 = {}
    dict2 = {}

    for item in magazine:
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1

    for item in ransom:
        if item in dict2:
            dict2[item] += 1
        else:
            dict2[item] = 1

    return(
            dict1,
            dict2
            )

def ransom_note(magazine, ransom):
    dict1, dict2 = generateDicts(magazine, ransom)

    for item in dict1:
        r = dict1.get(item, False)
        m = dict2.get(item, False)

        if m is False or m < r:
            return False

    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if(answer is True):
    print("Yes")
else:
    print("No")
