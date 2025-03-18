#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of integers n and m such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ m ≤ 2⋅10^6. Additionally, there is a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for each i. The sum of n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: Sasha or Anna based on the comparison between \(10^{max\_power}\) and the final value of `rev_res` after processing all test cases. The specific output depends on the values of `max_power` and `rev_res` for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of integers \(n\) and \(m\), and a list of \(n\) integers \(a_1, a_2, \ldots, a_n\). For each test case, it reverses each integer in the list, sorts the reversed integers, and then constructs a new string by alternating between non-same-length and same-length reversed integers. Finally, it compares \(10^{max\_power}\) with the constructed string and prints 'Sasha' if \(10^{max\_power}\) is less than the string, otherwise it prints 'Anna'.

