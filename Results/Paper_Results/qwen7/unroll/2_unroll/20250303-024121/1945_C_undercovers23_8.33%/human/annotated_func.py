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
        
    #State: The first element in the list `final` for each iteration, or 0 if no elements meet the criteria, or the full length of `s` if none of the elements meet the criteria and the percentage of '1's is less than 50.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) (number of test cases), an integer \( n \) (length of a binary string), and a binary string \( a \). For each test case, it calculates the number of positions in the string where the percentage of '1's and '0's both reach or exceed 50% for the first time. It then finds the position closest to half the length of the string (\( \frac{n}{2} \)) among these positions. If no such position exists, it returns either the full length of the string or 0 based on the percentage of '1's in the string. The function prints the closest position for each test case.

