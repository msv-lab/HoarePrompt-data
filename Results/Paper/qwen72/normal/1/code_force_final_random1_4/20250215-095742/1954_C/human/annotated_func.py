#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, x and y are integers where 1 ≤ x, y < 10^100, and both consist only of digits from 1 to 9.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 1000, `_` is `t - 1`, `a` and `b` are lists of integers representing the digits of the last input provided by the user, `i` is the index where `a[i]` is no longer equal to `b[i]` or `len(a)` (whichever is smaller). If `i` is not equal to the length of `a`, `new` is a list where each element up to index `i-1` is `max(a[j], b[j])` for `j` from 0 to `i-1`, and the rest are `None` values, and `new2` is a list where each element up to index `i-1` is `min(a[j], b[j])` for `j` from 0 to `i-1`, and the rest are `None` values. If `i` is equal to the length of `a`, `new` is a list where each element is `min(a[j], b[j])` for `j` from 0 to `len(a)-1`, and `new2` is a list where each element is `max(a[j], b[j])` for `j` from 0 to `len(a)-1.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads two lines of input, each representing a large integer (with digits from 1 to 9). It then constructs two new lists of digits, `new` and `new2`, such that up to the first differing digit position, `new` contains the maximum digit and `new2` contains the minimum digit from the corresponding positions in the input lists. After the first differing digit, `new` continues with the minimum digit and `new2` with the maximum digit. Finally, it prints the two resulting lists as strings. The function does not return any value; it only prints the results for each test case.

