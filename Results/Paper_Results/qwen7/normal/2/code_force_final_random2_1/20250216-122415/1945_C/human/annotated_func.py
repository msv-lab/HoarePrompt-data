#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'. The sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: final is a list of integers. Depending on the value of `t`, `final` will either contain the smallest index `ele` from `lst` where the absolute difference between `pk` and `ele` is equal to `mini`, or it will be an empty list followed by an element 0 if `c1` is greater than or equal to 50, or it will be an empty list followed by an element `n` if `c1` is less than 50.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a binary string `s` of length `n`. It calculates the percentage of '1's and '0's in the string up to every possible position and identifies positions where both percentages first reach or exceed 50%. From these positions, it selects the one closest to half the length of the string (`pk`). If no such position exists, it returns either the start or end of the string based on the overall percentage of '1's. The function outputs the selected position for each test case.

