#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 100, and the sequence of integers on the n cards is provided, where each integer is in the range 1 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `n` is an even integer such that 2 ≤ n ≤ 100, `a` is a list containing `n` input integers, `i` is `n - 1.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is an even integer such that 2 ≤ `n` ≤ 100, `a` is a list containing `n` input integers, and `d` is a dictionary where each key is a unique integer from `a` and the corresponding value is the count of occurrences of that integer in `a`.
    c = 0
    a1, a2 = -1, -1
    for i in d:
        if d[i] == n // 2:
            if c == 0:
                a1 = i
                c += 1
            else:
                a2 = i
                break
        
    #State of the program after the  for loop has been executed: `n` is an even integer such that 2 ≤ `n` ≤ 100; `a` is a list containing `n` input integers; `d` is a dictionary where each key is a unique integer from `a` with at least two keys having values equal to `n // 2`; `c` is 1 if one key had `d[i]` equal to `n // 2` and `a1` is set to that key; `c` is 2 if two keys had `d[i]` equal to `n // 2` with `a1` being the first and `a2` being the second key; if no keys matched, `a1` and `a2` remain -1.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 100; `a` is a list containing `n` input integers; `d` is a dictionary where each key is a unique integer from `a` with at least two keys having values equal to `n // 2`. If both `a1` and `a2` are not -1, then `c` is 2, the output is 'YES', and the values printed are `a1` and `a2`. If either `a1` is -1 or `a2` is -1 (or both), the output is 'NO'. In this case, `c` is either 1 if only one key had `d[i]` equal to `n // 2` or 0 if no keys matched, leaving `a1` and `a2` as -1.
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 100) and a sequence of `n` integers (where each integer is in the range 1 ≤ a_i ≤ 100). It counts the occurrences of each integer in the sequence and checks if there are exactly two distinct integers that both occur `n // 2` times. If such integers exist, it prints 'YES' followed by the two integers; otherwise, it prints 'NO'. The function does not handle cases where the input is invalid or out of the specified range.

