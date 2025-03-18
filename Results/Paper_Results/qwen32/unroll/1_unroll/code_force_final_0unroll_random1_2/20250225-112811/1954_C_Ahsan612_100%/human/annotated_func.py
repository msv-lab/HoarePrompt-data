#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9.
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
        
    #State: For each of the t test cases, there will be two output numbers: the first number is constructed by taking the maximum digit at each position until the first difference, then taking the minimum digit for all subsequent positions; the second number is constructed by taking the minimum digit at each position until the first difference, then taking the maximum digit for all subsequent positions.
#Overall this is what the function does:For each of the t test cases, the function takes two integers `x` and `y` consisting only of digits from 1 to 9, and outputs two numbers: the first number is constructed by taking the maximum digit at each position until the first difference, then taking the minimum digit for all subsequent positions; the second number is constructed by taking the minimum digit at each position until the first difference, then taking the maximum digit for all subsequent positions.

