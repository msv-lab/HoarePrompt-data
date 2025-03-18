I = lambda : list(map(int, input().split(' ')))
R = lambda : int(input())
for kp in range(int(input())):
    n = int(input())
    g = 0
    v1 = 0
    for i in range(1, n):
        v2 = i
        print(f'? {v1} {v1} {v2} {v2}')
        sys.stdout.flush()
        r = input('')
        if r == '<':
            v1 = v2
    prev = 0
    for i in range(1, n):
        print(f'? {v1} {i} {v1} {prev}')
        sys.stdout.flush()
        r = input()
        if r == '>':
            prev = i
    print(f'! {prev} {v1}')
    sys.stdout.flush()