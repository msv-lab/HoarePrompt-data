#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, x and y are integers for each test case such that 1 <= x, y < 10^100, and x and y consist only of digits from 1 to 9.
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
        
    #State: For each test case, the loop will output two lines. The first line will contain the maximum digit at each position from the two input numbers up to the point where the digits differ, and then the minimum digit for the remaining positions. The second line will contain the minimum digit at each position from the two input numbers up to the point where the digits differ, and then the maximum digit for the remaining positions. The variables `t`, `x`, and `y` will remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads two integers `x` and `y` from the input, where both integers are composed of digits from 1 to 9 and are less than 10^100. It then constructs two new integers: the first integer is formed by taking the maximum digit at each position from `x` and `y` up to the point where the digits differ, and the minimum digit for the remaining positions. The second integer is formed by taking the minimum digit at each position from `x` and `y` up to the point where the digits differ, and the maximum digit for the remaining positions. The function prints these two integers for each test case. The number of test cases `t` is read from the input at the beginning and remains unchanged throughout the function. The function does not return any value.

