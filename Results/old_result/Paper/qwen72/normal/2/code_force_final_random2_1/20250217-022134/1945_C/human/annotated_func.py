#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2·10^4, representing the number of test cases. For each test case, n is an integer such that 3 ≤ n ≤ 3·10^5, and a is a string of length n consisting only of '0' and '1'. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: After all iterations of the loop, `t` is reduced to 0, indicating that all test cases have been processed. For each test case, `n` and `s` are inputs specific to that test case, and `pk` is set to `n // 2`. The list `sl` contains the characters of the string `s`, `o` is the count of '1's in `sl`, and `z` is the count of '0's in `sl`. The variable `mini` holds the minimum absolute difference between `pk` and any valid index in `lst` where both `zero_perc` and `one_perc` are at least 50%. The list `lst` contains all such valid indices. The list `final` is a sorted list of the smallest indices from `lst` that have the minimum absolute difference with `pk`. If no such indices exist, `final` will contain either 0 or `n` based on whether the overall percentage of '1's in the string is at least 50%. The loop prints the first element of `final` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a binary string `s` of length `n`. For each test case, it calculates the position in the string where the cumulative percentage of '0's and '1's from the start to that position is at least 50% for both '0's and '1's. It then finds the position closest to the middle of the string (`n // 2`) that satisfies this condition and prints it. If no such position exists, it prints 0 if the overall percentage of '1's in the string is at least 50%, otherwise it prints `n`. The function processes up to 2·10^4 test cases, with the total length of all strings not exceeding 3·10^5.

