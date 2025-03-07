#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 2 · 10^4. For each test case, n is an integer representing the number of houses, where 3 ≤ n ≤ 3 · 10^5, and a is a string of length n consisting only of '0' and '1'. The sum of n over all test cases does not exceed 3 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        if n % 2 == 0:
            pk = n // 2
        else:
            pk = n // 2
        
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
            zero_perc = math.ceil(zero * 100 / (i + 1))
            one_perc = math.ceil((o - one) * 100 / (n - i - 1))
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
        
    #State: After all iterations of the loop, `t` is 0, `_` is `t - 1`, `n` is the last input integer, `s` is the last input string, `pk` is `n // 2`, `sl` is a list of characters from the last input string `s`, `o` is the number of times the character '1' appears in the last `sl`, `z` is the number of times the character '0' appears in the last `sl`, `mini` is the minimum of the absolute differences between `pk` and each element in `lst` across all iterations, `i` is `n - 1`, `zero` is the total number of '0's in the last `s`, `one` is the total number of '1's in the last `s`, `zero_perc` is `math.ceil(zero * 100 / (n - 1))`, `one_perc` is `math.ceil((o - one) * 100 / (n - i - 1))`, `lst` is a list of indices where both `zero_perc` and `one_perc` were at least 50% during the last iteration, `final` is a sorted list containing all elements from the last `lst` whose absolute difference with `pk` is equal to `mini`. If `len(final) == 0`, and `c1` (the integer division of `o * 100` by `n`) is greater than or equal to 50, `final` contains `[0]` and has a length of 1. If `len(final) == 0` and `c1` is less than 50, `final` contains the single element `n`, sorted in ascending order, and has a length of 1.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` representing the number of houses and a string `s` of length `n` consisting of '0' and '1'. The function then calculates and prints the smallest index (starting from 0) where the percentage of '0's up to that index and the percentage of '1's from that index to the end of the string are both at least 50%. If no such index exists, it prints 0 if the overall percentage of '1's is at least 50%, otherwise, it prints `n`.

