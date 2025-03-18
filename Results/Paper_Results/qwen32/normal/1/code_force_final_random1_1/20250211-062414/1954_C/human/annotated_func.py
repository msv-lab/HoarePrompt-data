#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, x and y are integers such that 1 ≤ x < 10^100 and 1 ≤ y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, x and y have the same length for each test case.
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
        
    #State: t remains the same, x and y are the last processed numbers, a and b are the last lists of digits, new and new2 are the final lists generated from the last pair of numbers.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` of the same length, consisting only of digits from 1 to 9. It then generates two new numbers: one where each digit is the maximum of the corresponding digits of `x` and `y`, and another where each digit is the minimum of the corresponding digits of `x` and `y`. The function prints these two new numbers for each test case.

