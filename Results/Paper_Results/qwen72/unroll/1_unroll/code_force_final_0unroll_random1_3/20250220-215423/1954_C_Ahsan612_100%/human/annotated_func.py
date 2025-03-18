#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, x and y are integers for each test case such that 1 <= x, y < 10^100, and x and y consist only of digits from 1 to 9.
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
        
    #State: For each test case, the loop prints two lines. The first line is the lexicographically largest number that can be formed by replacing the digits of the first number (x) with the maximum of the corresponding digits of x and y until the first differing digit, and then with the minimum of the corresponding digits for the rest of the digits. The second line is the lexicographically smallest number that can be formed by replacing the digits of the first number (x) with the minimum of the corresponding digits of x and y until the first differing digit, and then with the maximum of the corresponding digits for the rest of the digits. The variables t, x, and y remain unchanged.
#Overall this is what the function does:The function `func` reads input from the user for multiple test cases. For each test case, it takes two numbers `x` and `y` (represented as lists of digits), and prints two lines. The first line is the lexicographically largest number formed by replacing the digits of `x` with the maximum of the corresponding digits of `x` and `y` until the first differing digit, and then with the minimum of the corresponding digits for the rest of the digits. The second line is the lexicographically smallest number formed by replacing the digits of `x` with the minimum of the corresponding digits of `x` and `y` until the first differing digit, and then with the maximum of the corresponding digits for the rest of the digits. The function does not return any value. The variables `t`, `x`, and `y` remain unchanged after the function concludes.

