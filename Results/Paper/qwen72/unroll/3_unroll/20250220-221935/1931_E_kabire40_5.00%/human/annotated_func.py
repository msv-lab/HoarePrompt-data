#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and m are integers such that 1 ≤ n ≤ 2 × 10^5 and 0 ≤ m ≤ 2 × 10^6, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: The loop has finished executing all iterations, and the value of `rev_res` has been determined based on the input conditions. The variables `t`, `n`, `m`, and `a` remain unchanged as they are not modified within the loop. The output of the loop will be either 'Sasha' or 'Anna' for each test case, depending on whether the final value of `rev_res` exceeds \(10^{\text{max\_power}}\).
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads two integers `n` and `m` from input, followed by a list of `n` integers. It reverses each integer in the list, checks if the reversed integer has the same length as the original, and constructs a string `rev_res` by appending the original integers if their reversed form has the same length. If the reversed form has a different length, it appends these reversed integers to a list `rev_val`, sorts this list, and then alternates between appending the integers from `rev_val` and their reversed forms to `rev_res`. Finally, it compares the integer value of `rev_res` with \(10^m\). If `rev_res` exceeds \(10^m\), it prints 'Sasha'; otherwise, it prints 'Anna'. The function does not return any value.

