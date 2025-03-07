#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'. The sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 2⋅10^4. For each value of t, n is an integer read from input, s is a string read from input, and both zero and one are integers initialized to 0. The variable pk is calculated based on the value of n. The variable mini is set to 10^8. The list lst contains integers representing positions in the string s where the percentage of zeros and ones first meets or exceeds 50%. The list final contains the position from lst closest to pk. If no such position exists, final is set to either 0 or n based on the percentage of ones in s. The output is the first element of final for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a binary string \( s \) of length \( n \). For each test case, it calculates the positions in the string where the percentage of zeros and ones first meets or exceeds 50%. It then finds the position closest to half the length of the string (\( \frac{n}{2} \)). If no such position exists, it returns either the start or end of the string based on the overall percentage of ones in the string. The function outputs the position found for each test case.

