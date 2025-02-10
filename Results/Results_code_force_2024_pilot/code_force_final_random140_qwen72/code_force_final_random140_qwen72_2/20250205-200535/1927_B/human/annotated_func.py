#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers where each a_i satisfies 0 ≤ a_i < n.
def func_1(n, a):
    sam = 'abcdefghijklmnopqrstuvqwxyz'
    a_map = {x: (0) for x in range(n)}
    res = ''
    for i in range(n):
        beg = a_map[a[i]]
        
        res += sam[a_map[a[i]] % 27]
        
        a_map[a[i]] += 1
        
    #State: `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `a` is a list of n integers where each `a_i` satisfies 0 ≤ a_i < n, `sam` is the string 'abcdefghijklmnopqrstuvqwxyz', `a_map` is a dictionary mapping each integer from 0 to n-1 to the count of occurrences of that integer in the list `a`, `res` is a string composed of characters from `sam` based on the counts in `a_map` modulo 27, and the loop has completed all `n` iterations.
    return res
    #The program returns a string `res` composed of characters from the string 'abcdefghijklmnopqrstuvqwxyz' based on the counts in `a_map` modulo 27, where `a_map` maps each integer from 0 to n-1 to the count of occurrences of that integer in the list `a`.
#Overall this is what the function does:The function `func_1` takes a positive integer `n` and a list `a` of `n` integers, where each integer `a_i` satisfies 0 ≤ a_i < n. It returns a string `res` where each character is determined by the count of occurrences of each integer in `a`, mapped to characters from the string 'abcdefghijklmnopqrstuvqwxyz' based on their position, with counts taken modulo 27. The final state of the program includes the returned string `res` and the internal state of the function (such as the dictionary `a_map`) is not accessible outside the function.

