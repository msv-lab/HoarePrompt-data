#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses. The second line contains a string a of length n, consisting only of 0s and 1s, where a_j = 0 indicates the resident of the j-th house wants to live on the left side, and a_j = 1 indicates the resident wants to live on the right side. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: A series of integers, each representing the optimal split position for the corresponding test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string `a` of length `n` made up of '0's and '1's. It determines and prints the optimal split position for each test case, where the split ensures that at least 50% of the residents on each side of the split want to live on that side. If no such split exists, it returns either the start or end position based on the majority preference.

