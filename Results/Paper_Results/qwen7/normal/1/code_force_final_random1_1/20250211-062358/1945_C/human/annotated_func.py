#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'. The sum of all n over all test cases does not exceed 3⋅10^5.
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
        
    #State: After all iterations of the loop have finished, `pk` will be an integer representing half of the total input integer `t` (rounded down if `t` is odd). The variable `mini` will be an integer representing the minimum absolute difference between `pk` and any element in the list `lst`. The list `final` will contain the smallest element from `lst` that has the minimum absolute difference with `pk`. If no such element exists in `lst`, `final` will either contain 0 if the percentage of '1's in the string `s` is 50% or more, or it will contain `t` if the percentage of '1's is less than 50%.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \), an integer \( n \), and a binary string \( s \) of length \( n \). For each test case, it calculates the percentage of '1's and '0's in the string and identifies positions in the string where both percentages reach or exceed 50%. It then finds the position closest to half the length of the string \( n \) and returns this position. If no such position exists, it returns either the start or end of the string based on the majority percentage of '1's or '0's.

