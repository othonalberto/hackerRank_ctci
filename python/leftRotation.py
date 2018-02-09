def array_left_rotation(a, n, k):
    vec = [None]*n

    k = k % n
    newPosition = 0

    for i in range(0, n):
        newPosition = (n+i-k)%n
        vec[newPosition] = a[i]

    return vec

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
