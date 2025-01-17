def invert_bit(number):
    mask = 2147483647
    return ~number & mask
 
t = int(input())
for _ in range(t):
    n = int(input())
    list_a = list(map(int,input().split()))
    set_a = set(list_a)
    dict_invert_a = {}
    while list_a:
        a = list_a.pop(-1)
        if a in dict_invert_a:
            if dict_invert_a[a] > 0:
                dict_invert_a[a] -= 1
                n -= 1
                continue
        invert_a = invert_bit(a)
 
        if invert_a in set_a:
            if invert_a in dict_invert_a:
                dict_invert_a[invert_a] += 1
            else:
                dict_invert_a[invert_a] = 1
    print(n)