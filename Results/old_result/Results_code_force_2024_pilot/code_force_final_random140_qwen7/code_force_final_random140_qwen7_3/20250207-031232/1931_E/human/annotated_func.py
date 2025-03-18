#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ m ≤ 2⋅10^6; the list a contains n integers such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: After all iterations of the loop have finished, the variable `y` will be equal to the total number of test cases (`int(input())`), `rev_res` will be a string constructed by concatenating either the right-stripped version of every element in `operational_list` (if its index is even) or the unmodified version (if its index is odd), `list_len` will remain as the first input split by space, `max_power` will remain as the second input split by space, and `operational_list` will remain a list of strings sorted by the length of the string after removing trailing zeros. The final state of `rev_res` will be such that its length is greater than or equal to `int(max_power) + 1` if the condition `len(rev_res) >= int(max_power) + 1` is true for all iterations, otherwise, its length will be less than `int(max_power) + 1` for at least one iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two inputs: `list_len` and `max_power`. It then reads a list of strings, sorts this list based on the length of each string after removing trailing zeros, and constructs a new string `rev_res` by alternating between the right-stripped version of even-indexed strings and the unmodified version of odd-indexed strings. Finally, it checks if the length of `rev_res` is greater than or equal to `max_power + 1`. If the condition is met, it prints 'Sasha'; otherwise, it prints 'Anna'. The function does not return any value but prints the result for each test case.

