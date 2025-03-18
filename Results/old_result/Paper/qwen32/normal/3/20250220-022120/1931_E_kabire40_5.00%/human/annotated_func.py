#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n <= 2 * 10^5 and 0 <= m <= 2 * 10^6. The list a contains n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: - After all test cases are processed (i.e., the loop has executed `t` times), the final state will be that all test cases have been evaluated, and the appropriate output ("Sasha" or "Anna") has been printed for each test case.
    #
    #The final state of the loop variables after all iterations:
    #- `y` will be equal to `t` (the number of test cases).
    #- `rev_val` and `rev_res` will be reset for each test case and will not retain their values across different iterations.
    #- `list_len`, `max_power`, and `operational_list` will be re-initialized for each test case.
    #
    #Therefore, the final output state is:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives two integers `n` and `m`, and a list `a` of `n` integers. It then performs operations on the list, involving reversing some of the integers and sorting them, and finally compares a constructed value to `10` raised to the power of `m`. Based on this comparison, it prints either "Sasha" or "Anna" for each test case.

