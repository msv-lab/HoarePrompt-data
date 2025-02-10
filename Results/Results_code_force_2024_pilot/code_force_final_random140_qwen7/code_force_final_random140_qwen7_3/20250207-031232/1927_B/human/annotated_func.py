#State of the program right berfore the function call: n is a positive integer representing the length of the string, and a is a list of non-negative integers of length n, where 0 <= a_i < n for all i.
def func_1(n, a):
    sam = 'abcdefghijklmnopqrstuvqwxyz'
    a_map = {x: (0) for x in range(n)}
    res = ''
    for i in range(n):
        beg = a_map[a[i]]
        
        res += sam[a_map[a[i]] % 27]
        
        a_map[a[i]] += 1
        
    #State: Output State: `i` is 26; `n` is 26; `res` is the concatenation of `sam[a_map[a[i]] % 27]` for all `i` from 0 to 25; `beg` is `a_map[a[25]]`; `a_map[a[25]]` is increased by 1.
    #
    #In this final state, the variable `i` reaches the value of `n`, which is 26. The string `res` contains 26 characters, each being `sam[a_map[a[i]] % 27]` for `i` ranging from 0 to 25. After the loop completes, `a_map[a[25]]` is incremented by 1.
    return res
    #The program returns a string `res` that is the concatenation of `sam[a_map[a[i]] % 27]` for all `i` from 0 to 25, where `i` starts at 26 and `n` is also 26, and `a_map[a[25]]` is incremented by 1 after the loop completes.
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the length of the string, and `a`, a list of non-negative integers of length `n`. It returns a string `res` that is the concatenation of characters from the string `sam` based on the values in `a_map` modulo 27. After processing all elements in `a`, it increments the value in `a_map` corresponding to the last element in `a` by 1.

