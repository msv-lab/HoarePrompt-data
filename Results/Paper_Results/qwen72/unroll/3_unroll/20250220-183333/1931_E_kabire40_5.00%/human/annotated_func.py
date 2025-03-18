#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ m ≤ 2 · 10^6. The list a contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it processes the list of integers, reverses them, and constructs a new string `rev_res`. If the length of the reversed number is the same as the original, it is directly appended to `rev_res`. Otherwise, the reversed number is added to a list `rev_val`. After processing all numbers, `rev_val` is sorted, and its elements are alternately appended to `rev_res` in their original and reversed forms. Finally, if the integer value of `rev_res` is greater than \(10^{\text{max\_power}}\), it prints 'Sasha'; otherwise, it prints 'Anna'. The variables `t`, `n`, `m`, and `a` remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads two integers `n` and `m`, and a list of `n` integers. It constructs a new string `rev_res` by reversing the integers in the list. If the reversed integer has the same length as the original, it is appended directly to `rev_res`. Otherwise, the reversed integer is added to a list `rev_val`. After processing all integers, `rev_val` is sorted, and its elements are alternately appended to `rev_res` in their original and reversed forms. Finally, if the integer value of `rev_res` exceeds \(10^{\text{max\_power}}\), it prints 'Sasha'; otherwise, it prints 'Anna'. The function does not return any value and does not modify the input variables `t`, `n`, `m`, or `a`.

