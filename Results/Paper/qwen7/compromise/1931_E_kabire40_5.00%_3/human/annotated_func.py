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
        
    #State: After all iterations of the loop, `rev_res` is a string that alternates between the integer values of `rev_val` and their reversed forms, starting with the first element of `rev_val` and ending with its last element. If the final value of `rev_res` is greater than \(10^{\text{int(max_power)}}\), the loop prints 'Sasha'; otherwise, it prints 'Anna'.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two inputs: the length of a list and the maximum power of 10. It then reads a list of integers. The function reverses each integer in the list and constructs a new string by alternating between the original reversed integers and their normal form, starting with the first reversed integer. Finally, it compares this constructed string (interpreted as an integer) with \(10\) raised to the power of the maximum power read. If the constructed integer is greater, it prints 'Sasha'; otherwise, it prints 'Anna'. The function does not return any value but prints the result for each test case.

