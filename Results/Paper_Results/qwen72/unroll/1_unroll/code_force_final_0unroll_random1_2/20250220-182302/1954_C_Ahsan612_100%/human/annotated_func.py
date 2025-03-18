#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, x and y are integers for each test case, where 1 <= x < 10^100 and 1 <= y < 10^100, and x and y consist only of digits from 1 to 9.
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
        
    #State: The loop will execute `t` times, and for each iteration, it will read two lines of input representing the integers `x` and `y` as lists of digits. For each pair of integers, it will print two lines: the first line will be the maximum digit at each position until the first differing digit, followed by the minimum digit for the remaining positions. The second line will be the minimum digit at each position until the first differing digit, followed by the maximum digit for the remaining positions. The variables `t`, `x`, and `y` will remain unchanged, but the loop will have processed `t` test cases.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer such that 1 <= t <= 1000. For each test case, it reads two integers `x` and `y` (1 <= x, y < 10^100, consisting only of digits from 1 to 9) as lists of digits. It then constructs two new lists of digits: the first list contains the maximum digit at each position until the first differing digit, followed by the minimum digit for the remaining positions; the second list contains the minimum digit at each position until the first differing digit, followed by the maximum digit for the remaining positions. The function prints these two lists as strings for each test case. The function does not return any value. After execution, the variables `t`, `x`, and `y` remain unchanged, but the function has processed `t` test cases and printed the results.

