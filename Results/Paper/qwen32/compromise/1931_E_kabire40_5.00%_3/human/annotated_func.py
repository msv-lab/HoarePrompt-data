#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and m is an integer such that 0 <= m <= 2 * 10^6. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of n across all test cases does not exceed 2 * 10^5.
def func():
    for y in range(int(input())):
        rev_val = []
        
        rev_res = ''
        
        list_len, max_power = input().split()
        
        operational_list = input().split()
        
        for x in operational_list:
            x_rev = int(x[::-1])
            if len(str(x_rev)) == len(x):
                rev_res = rev_res + x
            else:
                rev_val.append(x[::-1])
        
        rev_val.sort()
        
        for x in range(len(rev_val)):
            if x % 2 == 0:
                val_in = int(rev_val[x])
                rev_res += str(val_in)
            else:
                val_in = rev_val[x]
                rev_res += val_in[::-1]
        
        if 10 ** int(max_power) < int(rev_res):
            print('Sasha')
        else:
            print('Anna')
        
    #State: A series of "Sasha" or "Anna" printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `m`, and a list `a` of `n` integers. For each test case, it determines whether to print "Sasha" or "Anna" based on the reversed values of the integers in `a` and the value of `m`. Specifically, it reverses each integer in `a`, sorts the reversed integers of certain lengths, and constructs a result string. If the integer value of this result string exceeds `10` raised to the power of `m`, it prints "Sasha"; otherwise, it prints "Anna".

