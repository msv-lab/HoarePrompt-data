#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ m ≤ 2⋅10^6; the list a contains n integers such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: Sasha or Anna, depending on the input values provided during the loop executions. The final output will be either 'Sasha' or 'Anna' based on the comparison between `rev_res` and `10 ** int(max_power)`. If `rev_res` is greater than `10 ** int(max_power)`, 'Sasha' is printed; otherwise, 'Anna' is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t, two integers n and m, and a list a containing n integers. For each test case, it reverses the digits of each integer in the list, sorts the reversed integers, and then reconstructs a new string by alternating between the sorted reversed integers and their original reversed forms. Finally, it compares this reconstructed string (converted to an integer) with \(10^{max\_power}\), where \(max\_power\) is derived from the input. If the reconstructed string is greater, it prints 'Sasha'; otherwise, it prints 'Anna'.

