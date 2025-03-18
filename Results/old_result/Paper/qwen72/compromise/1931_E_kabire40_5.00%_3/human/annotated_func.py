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
        
    #State: `y` is `int(input()) - 1`, `int(input())` is a positive integer, `list_len` is the first part of the input string, `max_power` is the second part of the input string, `operational_list` is a list of strings with at least one element, `x` is the last element of `rev_val`, `x_rev` is the integer value of the reversed string of the last element of `operational_list`, `rev_val` is a sorted list containing the reversed strings of all elements in `operational_list` whose reversed integer values have a different string length compared to their original string length, and `rev_res` is a string that contains the concatenated results of the loop, where for each even index in `rev_val`, the integer value of the element is appended to `rev_res`, and for each odd index, the reversed string of the element is appended to `rev_res`. If the integer value of `rev_res` is greater than \(10\) raised to the power of the integer value of `max_power`, then the integer value of `rev_res` is greater than \(10\) raised to the power of the integer value of `max_power`. Otherwise, the integer value of `rev_res` is less than or equal to \(10\) raised to the power of the integer value of `max_power`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers `list_len` and `max_power`, and a list of `list_len` integers. It reverses each integer in the list, and if the reversed integer has the same length as the original, it appends the original integer to a result string. If the reversed integer has a different length, it appends the reversed integer to a list. This list is then sorted, and for each element in the sorted list, it appends the integer value to the result string if the index is even, and the reversed string if the index is odd. Finally, it compares the integer value of the result string to \(10\) raised to the power of `max_power` and prints 'Sasha' if the result string's integer value is greater, otherwise it prints 'Anna'. The function does not return any value.

