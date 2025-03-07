#State of the program right berfore the function call: The function `func` is expected to process multiple test cases. Each test case includes an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident who wants to live on the left side of the street and '1' indicates a resident who wants to live on the right side. The function should determine the optimal position `i` to lay the road such that at least half of the residents on each side of the street are satisfied with their side, and the road is as close to the middle of the village as possible. The function should return the position `i` for each test case.
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
        
    #State: After all iterations of the loop, `t` is 0 (since the loop has completed its `t` iterations). For each iteration, the variables `n`, `s`, `sl`, `pk`, `o`, `z`, `zero`, `one`, `zero_perc`, `one_perc`, `i`, `lst`, `mini`, and `final` are recalculated based on the new inputs provided for each test case. Specifically, `mini` will be the minimum value of `abs(pk - ele)` for all elements `ele` in `lst` for each test case. The variable `ele` will be the last element processed from `lst` for each test case. The list `final` will contain all elements from `lst` that have an absolute difference with `pk` equal to `mini`, and `final` will be sorted in ascending order for each test case. If the length of `final` is 0 for any test case, the list remains empty. If the length of `final` is 1, and if `c1` (which is equal to `o * 100 // n`) is greater than or equal to 50, the first element of `final` is 0. Otherwise, the first element of `final` is `n`. The final output for each test case is the first element of `final`.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `n` (representing the number of houses) and a string `a` (indicating the preferred side of the street for each resident). For each test case, the function determines the optimal position `i` to lay a road such that at least half of the residents on each side of the street are satisfied with their side, and the road is as close to the middle of the village as possible. The function prints the optimal position `i` for each test case. If no such position exists, it prints either 0 or `n` depending on the majority preference of the residents.

