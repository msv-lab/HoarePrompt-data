#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'. The sum of all n values across all test cases does not exceed 3⋅10^5.
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
        
    #State: The final output state after the loop executes all iterations will be a list stored in `final`. This list will contain the smallest index `ele` from `lst` where the absolute difference between `pk` (which is `n // 2`) and `ele` is minimized. If there are multiple such indices, all these indices will be included in the list. If no such indices exist (i.e., `lst` is empty), then `final` will either be `[0]` if more than half of the characters in `s` are '1', or `[n]` if more than half of the characters are '0' and `final` is still empty. The list `final` will be sorted.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a positive integer \( t \) indicating the number of subsequent test cases, an integer \( n \) representing the length of a binary string \( a \), and the string \( a \) itself. It calculates the percentage of '1's and '0's in the string up to each position and identifies the positions where both percentages first reach or exceed 50%. From these positions, it selects the one closest to the middle of the string (\( n // 2 \)). If no such position exists, it returns either the start or the end of the string based on which has more than half of the characters being '1' or '0', respectively. The function outputs the selected position(s) for each test case.

