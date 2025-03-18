#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ 10^4, a is a list of n integers where 1 ≤ a_i ≤ 10^4, and s is a string of length n consisting only of the characters 'L' and 'R'.
def func_1(n, m, a, s):
    b = []
    l = 0
    r = n - 1
    for i in range(n):
        if s[i] == 'L':
            b.append(a[l])
            l += 1
        else:
            b.append(a[r])
            r -= 1
        
    #State: `n` and `m` are positive integers such that 1 ≤ `n` ≤ 2·10^5 and 1 ≤ `m` ≤ 10^4, `a` is a list of `n` integers where 1 ≤ `a_i` ≤ 10^4, `s` is a string of length `n` consisting only of the characters 'L' and 'R', `b` is a list containing all elements of `a` in an order determined by the characters in `s`, `l` is `n` if all characters in `s` are 'L', otherwise it is the number of 'L' characters in `s`, `r` is -1 if all characters in `s` are 'R', otherwise it is `n - 1 -` the number of 'R' characters in `s`, and `i` is `n - 1`.
    ans = []
    p = 1
    for v in reversed(b):
        p = p * v % m
        
        ans.append(p)
        
    #State: `n` and `m` are positive integers such that 1 ≤ `n` ≤ 2·10^5 and 1 ≤ `m` ≤ 10^4, `a` is a list of `n` integers where 1 ≤ `a_i` ≤ 10^4, `s` is a string of length `n` consisting only of the characters 'L' and 'R', `b` is a list containing all elements of `a` in an order determined by the characters in `s`, `l` is `n` if all characters in `s` are 'L', otherwise it is the number of 'L' characters in `s`, `r` is -1 if all characters in `s` are 'R', otherwise it is `n - 1 -` the number of 'R' characters in `s`, `i` is `n - 1`, `ans` is a list containing `n` elements, each element being the cumulative product of the elements in `b` from the last to the current index, modulo `m`, and `p` is the final cumulative product of all elements in `b`, modulo `m`.
    return reversed(ans)
    #The program returns a reversed list `ans`, which contains `n` elements. Each element in `ans` represents the cumulative product of the elements in `b` from the last to the current index, taken modulo `m`. The list `ans` is reversed, meaning the first element of the returned list corresponds to the last element of the original `ans` list, and so on.
#Overall this is what the function does:The function `func_1` takes four parameters: `n` (a positive integer), `m` (a positive integer), `a` (a list of `n` integers), and `s` (a string of length `n` consisting of 'L' and 'R' characters). It returns a list of `n` integers, where each integer is the cumulative product of the elements in a reordered list `b` from the last to the current index, taken modulo `m`. The list `b` is constructed by rearranging the elements of `a` based on the characters in `s`: if `s[i]` is 'L', the element from the start of `a` is added to `b`; if `s[i]` is 'R', the element from the end of `a` is added to `b`. The final list is reversed before being returned.

