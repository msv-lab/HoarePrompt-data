#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ m ≤ 2 · 10^6. The list a contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has finished executing all iterations, and for each test case, the output will be either 'Sasha' or 'Anna' based on the conditions specified in the loop. The variables `t`, `n`, `m`, and the list `a` remain unchanged as they are not modified within the loop. The loop processes the input values and prints the result for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `m`, and a list of `n` integers. For each test case, it reverses each integer in the list, checks if the reversed integer has the same number of digits as the original, and constructs a string `rev_res` by appending the original integers that have the same number of digits when reversed and the reversed integers that do not. It then sorts the reversed integers that were not appended directly and alternates between appending them directly and appending them in their original form to `rev_res`. Finally, it compares the integer value of `rev_res` with `10^m` and prints 'Sasha' if `rev_res` is greater, otherwise it prints 'Anna'. The function does not return any value; it only prints the result for each test case. The input variables `t`, `n`, `m`, and the list `a` are not modified by the function.

