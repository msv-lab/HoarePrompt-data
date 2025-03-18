#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2·10^4. For each test case, n is an integer such that 3 ≤ n ≤ 3·10^5, and a is a string of length n consisting only of the characters '0' and '1'. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: [result1, result2, ..., resultt]
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a binary string `a` of length `n`. For each test case, it calculates and prints the smallest index `i` such that the percentage of '0's up to index `i` and the percentage of '1's from index `i+1` to the end are both at least 50%. If no such index exists, it prints `0` if the total percentage of '1's in the string is at least 50%, otherwise it prints `n`.

