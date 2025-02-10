#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of two lines: the first line contains two integers n and m where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ m ≤ 2 · 10^6, representing the number of integers in the list and the parameter determining when Sasha wins, respectively. The second line contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, representing the list of integers. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `y` is `t - 1`, `list_len` is a positive integer, `max_power` is the second part of the input, `operational_list` is a sorted list of strings from the input, `x` is `list_len - 1`. `rev_res` is the concatenation of all elements in `operational_list` where elements at even indices (0-based) have trailing zeros removed, and elements at odd indices are concatenated as they are. If the length of `rev_res` is greater than or equal to the integer value of `max_power` plus one, the condition is met, and "Sasha" is printed. Otherwise, the length of `rev_res` is less than `int(max_power) + 1`, and "Anna" is printed.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of integers `n` and a parameter `m`, followed by a list of `n` integers. It then constructs a string `rev_res` by concatenating the elements of the list, removing trailing zeros from elements at even indices and leaving elements at odd indices unchanged. If the length of `rev_res` is greater than or equal to `m + 1`, it prints "Sasha"; otherwise, it prints "Anna". After processing all test cases, the function completes, and the final state includes the printed results for each test case.

