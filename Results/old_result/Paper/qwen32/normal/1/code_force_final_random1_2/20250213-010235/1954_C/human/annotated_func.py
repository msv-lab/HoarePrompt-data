#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, for each test case, x and y are integers such that 1 ≤ x < 10^100 and 1 ≤ y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, x and y have the same length within each test case.
def func():
    for _ in range(int(input())):
        a = list(map(int, list(input())))
        
        b = list(map(int, list(input())))
        
        new = [None] * len(a)
        
        new2 = [None] * len(a)
        
        i = 0
        
        while i < len(a) and a[i] == b[i]:
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
        
        if i != len(a):
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
            while i < len(a):
                new[i] = min(a[i], b[i])
                new2[i] = max(a[i], b[i])
                i += 1
        
        print(''.join(str(x) for x in new))
        
        print(''.join(str(x) for x in new2))
        
    #State: The final `new` and `new2` lists are identical to the last `a` and `b` lists processed in the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two integers `x` and `y` of the same length and composed only of digits from 1 to 9. For each test case, it generates two new numbers: one formed by taking the maximum digit at each position between `x` and `y`, and another formed by taking the minimum digit at each position between `x` and `y`. It then prints these two new numbers for each test case.

