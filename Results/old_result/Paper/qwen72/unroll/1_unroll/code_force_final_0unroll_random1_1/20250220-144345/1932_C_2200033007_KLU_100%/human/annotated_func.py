#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2·10^5), m is a positive integer (1 ≤ m ≤ 10^4), a is a list of n positive integers (1 ≤ a_i ≤ 10^4), and s is a string of n characters, each being either 'L' or 'R'.
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
        
    #State: n is a positive integer (1 ≤ n ≤ 2·10^5), m is a positive integer (1 ≤ m ≤ 10^4), a is a list of n positive integers (1 ≤ a_i ≤ 10^4), s is a string of n characters, each being either 'L' or 'R', b is a list of n integers where the elements are rearranged based on the characters in s, l is n, r is -1.
    ans = []
    p = 1
    for v in reversed(b):
        p = p * v % m
        
        ans.append(p)
        
    #State: `n` is a positive integer (1 ≤ n ≤ 2·10^5), `m` is a positive integer (1 ≤ m ≤ 10^4), `a` is a list of n positive integers (1 ≤ a_i ≤ 10^4), `s` is a string of n characters, each being either 'L' or 'R', `b` is a list of n integers where the elements are rearranged based on the characters in `s`, `l` is n, `r` is -1, `ans` is a list of n integers where each element is the cumulative product of the elements in `b` taken in reverse order modulo `m`, `p` is the product of all elements in `b` modulo `m`.
    return reversed(ans)
    #The program returns the list `ans` in reversed order, where `ans` is a list of n integers, each representing the cumulative product of the elements in `b` taken in reverse order, modulo `m`. The list `b` contains the elements of `a` rearranged based on the characters in `s`, and `p` is the product of all elements in `b` modulo `m`.
#Overall this is what the function does:The function `func_1` accepts four parameters: `n` (a positive integer), `m` (a positive integer), `a` (a list of `n` positive integers), and `s` (a string of `n` characters, each being either 'L' or 'R'). It returns a list `ans` of `n` integers, where each element in `ans` represents the cumulative product of the elements in `b` taken in reverse order, modulo `m`. The list `b` is a rearrangement of the elements in `a` based on the characters in `s`: if the character is 'L', the element from the start of `a` is used; if the character is 'R', the element from the end of `a` is used. The final state of the program after the function concludes is that `ans` is a list of `n` integers, each representing the cumulative product of the elements in `b` in reverse order, modulo `m`.

