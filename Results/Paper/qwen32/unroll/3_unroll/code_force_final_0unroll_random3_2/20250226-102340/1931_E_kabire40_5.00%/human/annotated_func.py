#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of two lines: the first line contains integers n and m such that 1 <= n <= 2 * 10^5 and 0 <= m <= 2 * 10^6. The second line contains n integers a_1, a_2, ..., a_n such that 1 <= a_i <= 10^9. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: A series of 'Sasha' or 'Anna' prints, one for each test case, based on the comparison of the constructed integer with 10^m for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of integers and an integer `m`. For each test case, it constructs a new integer by reversing some of the integers in the list according to specific rules and then compares this constructed integer to `10^m`. It prints 'Sasha' if the constructed integer is greater than `10^m` and 'Anna' otherwise.

