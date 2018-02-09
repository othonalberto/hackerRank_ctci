def is_matched(expression):
    if expression is None:
        return False

    n = 0

    stack = []

    for char in expression:
        n = n + 1

        if (char == '{'):
            stack.append('}')
        elif (char == '('):
            stack.append(')')
        elif (char == '['):
            stack.append(']')
        else:
            n = n - 1
            if (stack == [] or char != stack[n-1]):
                return False
            
            stack.pop()

            n = n - 1

    if stack == []:
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
