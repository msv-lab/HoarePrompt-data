#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 2·10^4. For each test case, n is an integer representing the number of houses, where 3 ≤ n ≤ 3·10^5, and a is a string of length n consisting only of '0' and '1'. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: After all iterations of the loop, `t` is 0, `n` has been processed for all test cases, `s` has been processed for all test cases, `pk` is the middle index of `n` for the last processed test case, `sl` is the list of characters from the last processed string `s`, `o` is the count of '1's in `sl` for the last processed test case, `z` is the count of '0's in `sl` for the last processed test case, `mini` is the minimum absolute difference between `pk` and any element in `lst` for the last processed test case, `i` is `n - 2` for the last processed test case, `zero` is the total number of '0's encountered in the string `s` up to the second-to-last character for the last processed test case, `one` is the total number of '1's encountered in the string `s` up to the second-to-last character for the last processed test case, `zero_perc` is `math.ceil(zero * 100 / (n - 1))` for the last processed test case, `one_perc` is `math.ceil((o - one) * 100 / (n - (n - 2) - 1))` for the last processed test case, `lst` contains all indices `i + 1` where both `zero_perc` and `one_perc` were greater than or equal to 50 during the loop execution for the last processed test case, `final` is a sorted list containing all elements from `lst` whose absolute difference with `pk` is equal to `mini` for the last processed test case. If `len(final) == 0`, then `c1` is `o * 100 // n` for the last processed test case. If `c1` is greater than or equal to 50, `final` now includes the value 0. Otherwise, if `c1` is less than 50, `final` now includes `n`. The final output for each test case is the first element of `final` for that test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` (3 ≤ n ≤ 3·10^5) and a string `s` of length `n` consisting of '0' and '1'. For each test case, it calculates the optimal position to split the string such that the percentage of '0's and '1's in both halves is at least 50%, or it determines the closest position to the middle of the string that meets this condition. If no such position exists, it checks the overall percentage of '1's in the string and outputs 0 if the percentage is 50% or more, otherwise it outputs the length of the string `n`. The function prints the result for each test case.

