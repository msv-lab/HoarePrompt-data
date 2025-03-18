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
        
    #State: After all iterations of the loop, `rev_res` is a string that concatenates the integer representations of even-indexed elements from `rev_val` and the reversed versions of odd-indexed elements from `rev_val`, in the order they appear in `rev_val`. This process is repeated for each test case until all test cases are processed. The final `rev_res` for each test case is determined based on the rules described in the loop body, and it does not depend on whether \(10^{int(max_power)}\) is less than the integer value represented by `rev_res` or not.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers (list length and maximum power) and a list of integers. It reverses each integer in the list, sorts the reversed integers, and then constructs a new string by concatenating every even-indexed reversed integer and the reverse of every odd-indexed reversed integer. Finally, it compares this constructed string (interpreted as an integer) with \(10^{max\_power}\), printing 'Sasha' if the constructed string is greater, and 'Anna' otherwise. This process is repeated for each test case.

