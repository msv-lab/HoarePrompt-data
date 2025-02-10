#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of two lines: the first line contains two integers n and m where 1 ≤ n ≤ 2 × 10^5 and 0 ≤ m ≤ 2 × 10^6, representing the number of integers in the list and the parameter determining when Sasha wins, respectively. The second line contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, representing the list of integers. The sum of n over all test cases does not exceed 2 × 10^5.
def func():
    for y in range(int(input())):
        rev_res = ''
        
        list_len, max_power = input().split()
        
        operational_list = sorted(input().split(), key=lambda x: len(x.rstrip('0')) -
            len(x))
        
        for x in range(int(list_len)):
            if x % 2 == 0:
                rev_res += operational_list[x].rstrip('0')
            else:
                rev_res += operational_list[x]
        
        if len(rev_res) >= int(max_power) + 1:
            print('Sasha')
        else:
            print('Anna')
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `y` is `t` - 1, `list_len` is a positive integer, `max_power` is the second part of the input provided, `operational_list` is a list of strings sorted by the difference between the length of the string without trailing zeros and the original length of the string, `x` is `list_len` - 1, and `rev_res` is the concatenation of all strings in `operational_list` where strings at even indices (0-based) have their trailing zeros removed, and strings at odd indices are concatenated as they are. If the length of `rev_res` is greater than or equal to `int(max_power) + 1`, the condition is met. Otherwise, the length of `rev_res` is less than `int(max_power) + 1.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a list of integers and a threshold value. It constructs a string by concatenating the elements of the list, removing trailing zeros from elements at even indices. If the resulting string's length meets or exceeds the threshold plus one, it prints "Sasha"; otherwise, it prints "Anna". The function handles multiple test cases and outputs the result for each.

