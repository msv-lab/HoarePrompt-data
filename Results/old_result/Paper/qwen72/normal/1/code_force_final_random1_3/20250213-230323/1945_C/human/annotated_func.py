#State of the program right berfore the function call: The function `func` is intended to solve a problem involving a series of test cases, each containing a string `a` of length `n` (3 ≤ n ≤ 3·10^5), where `a` consists only of '0' and '1'. The function should determine the optimal position `i` to place a road such that at least half of the residents on each side of the road are satisfied with their side, and `i` should be as close to the middle of the village as possible. The function is expected to handle multiple test cases, with the total number of test cases `t` (1 ≤ t ≤ 2·10^4) and the sum of all `n` values not exceeding 3·10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        if n % 2 == 0:
            pk = n / 2
        else:
            pk = n / 2
        
        sl = list(s)
        
        o = sl.count('1')
        
        z = sl.count('0')
        
        zero, one = 0, 0
        
        lst = []
        
        mini = pow(10, 8)
        
        for i in range(n - 1):
            if s[i] == '0':
                zero += 1
            else:
                one += 1
            zero_perc = zero * 100 // (i + 1)
            one_perc = (o - one) * 100 // (n - i - 1)
            if zero_perc >= 50 and one_perc >= 50:
                lst.append(i + 1)
        
        for ele in lst:
            mini = min(mini, abs(pk - ele))
        
        final = []
        
        for elem in lst:
            if abs(pk - elem) == mini:
                final.append(elem)
        
        final.sort()
        
        if len(final) == 0:
            c1 = o * 100 // n
            if c1 >= 50:
                final.append(0)
            else:
                final.append(n)
        
        print(final[0])
        
    #State: After all iterations of the loop, `t` is 0, `n` is the last input integer, `s` is the last input string, `sl` is a list containing the characters of the last `s`, `pk` is `n / 2`, `o` is the number of times '1' appears in the last `sl`, `z` is the number of times '0' appears in the last `sl`, `mini` is the minimum of the initial `mini` and the absolute differences between `pk` and each element in `lst` across all iterations, `i` is `n - 2` for the last iteration, `zero` is the number of '0's in the first `n - 1` characters of the last `s`, `one` is the number of '1's in the first `n - 1` characters of the last `s`, `zero_perc` is `zero * 100 // (n - 1)` for the last iteration, `one_perc` is `(o - one) * 100 // 1` for the last iteration, `lst` contains all indices `i + 1` where both `zero_perc` and `one_perc` are at least 50% for the last iteration, `final` is a sorted list containing all elements `elem` from the last `lst` where `abs(pk - elem) == mini`. If the length of `final` is 0, `c1` is `o * 100 // n` for the last iteration. If `c1` is greater than or equal to 50, `final` includes the element 0. If `c1` is less than 50, `final` includes the value `n`.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by an integer `n` and a binary string `s` of length `n`. For each test case, it determines the optimal position `i` to place a road such that at least half of the residents on each side of the road are satisfied with their side, and `i` is as close to the middle of the village as possible. The function prints the optimal position for each test case. If no such position exists, it prints the position that maximizes the satisfaction of the majority, either at the start (0) or the end (`n`) of the village.

