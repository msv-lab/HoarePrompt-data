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
        
    #State: `y` is `int(input()) - 1`, `operational_list` is a list of strings from the input, `list_len` and `max_power` are assigned the values from the input split by a space, `x` is the length of `rev_val` minus 1, `rev_res` is a string containing all the strings from `operational_list` that, when reversed, have the same length as the original string, concatenated together, plus the string representations of the even-indexed elements in `rev_val` and the reversed values of the odd-indexed elements in `rev_val`, `rev_val` is a sorted list containing the reversed strings of all the strings from `operational_list` that, when reversed, have a different length than the original string. If `10
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` and an integer `m`. For each test case, it reads a list of `n` integers, reverses each integer, and constructs a string `rev_res` based on specific conditions. If the reversed integer has the same length as the original integer, it is directly appended to `rev_res`. If the reversed integer has a different length, it is stored in a list `rev_val`. After processing all integers, `rev_val` is sorted, and its elements are appended to `rev_res` in an alternating manner: even-indexed elements are appended as is, and odd-indexed elements are appended in their reversed form. Finally, the function compares the integer value of `rev_res` with `10^m` and prints 'Sasha' if `rev_res` is greater, otherwise prints 'Anna'. The function does not return any value.

