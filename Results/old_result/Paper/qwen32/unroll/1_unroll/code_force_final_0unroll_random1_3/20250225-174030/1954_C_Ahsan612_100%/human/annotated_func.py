#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, x and y have the same length for each test case.
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
        
    #State: For each test case, two strings of the same length as the input strings x and y are printed, where the first differing digit positions have the maximum and minimum of x and y assigned to new and new2 respectively, and all subsequent digits have the minimum and maximum of x and y assigned to new and new2 respectively. This process is repeated t times for t test cases.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `x` and `y` of the same length, composed only of digits from 1 to 9. For each test case, it generates two new numbers: one where the digits are the maximum of the corresponding digits in `x` and `y` up to the first differing position, followed by the minimum of the remaining digits, and another where the digits are the minimum of the corresponding digits in `x` and `y` up to the first differing position, followed by the maximum of the remaining digits. It prints these two numbers for each test case.

