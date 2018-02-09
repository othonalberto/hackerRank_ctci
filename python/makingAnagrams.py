def dicts(a, b, dic1, dic2):
    for item in a:
        if item in dic1:
            dic1[item] += 1
        else:
            dic1[item] = 1

    for item in b:
        if item in dic2:
            dic2[item] += 1
        else:
            dic2[item] = 1

def compare(dic1, dic2):
    count = 0

    for item in dic1:
        t = dic1.get(item, False)
        other_t = dic2.get(item, False)

        if other_t is not False and other_t > 0:

            if other_t > t:
                dic2[item] = t
                count += other_t - t
            elif t > other_t:
                dic1[item] = dic2[item]
                count += t - other_t
        else:
            dic1[item] = 0
            count += t

    return count

def number_needed(a, b):
        dic1 = {}
        dic2 = {}

        count = 0

        dicts(a, b, dic1, dic2)

        count = compare(dic1, dic2)
        count += compare(dic2, dic1)

        return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))
