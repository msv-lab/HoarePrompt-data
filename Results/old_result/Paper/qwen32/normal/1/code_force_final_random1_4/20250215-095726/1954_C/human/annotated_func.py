#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, x and y are integers consisting only of digits from 1 to 9, and they have the same length. Additionally, 1 ≤ x < 10^100 and 1 ≤ y < 10^100.
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
        
    #State: 
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `x` and `y` of the same length, composed solely of digits from 1 to 9. For each test case, it generates two new numbers: one where digits are taken as the maximum of corresponding digits from `x` and `y`, and another where digits are taken as the minimum of corresponding digits from `x` and `y`. These two new numbers are printed for each test case.

