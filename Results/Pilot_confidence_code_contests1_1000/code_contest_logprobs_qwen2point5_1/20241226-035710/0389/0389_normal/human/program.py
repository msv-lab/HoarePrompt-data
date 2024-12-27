for i in range(int(raw_input())):
    n, r = map(int, raw_input().split())
    xs = map(int, raw_input().split())
    result = 1
    push = r
    xs = sorted(set(xs))

    j = len(xs) - 2
    while xs[j] - push > 0 and j >= 0:
        result += 1
        push += r
        j -= 1 
     
    print(result)