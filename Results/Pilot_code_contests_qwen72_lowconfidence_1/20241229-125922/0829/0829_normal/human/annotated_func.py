#State of the program right berfore the function call: The input is a string `s` of length `n` where 1 ≤ n ≤ 10^6, and `s` consists of characters "*", "?", and digits "0", "1", or "2".
def func():
    t = None
    line = raw_input()
    big_prime = 1000000007
    for c in line:
        if t is None:
            zero = 1
            one_used = 0
            one_unused = 1
            two = 0
            mine = 1
        else:
            zero = (t[0] + t[1]) % big_prime
            one_used = t[4]
            one_unused = (t[0] + t[1]) % big_prime
            two = t[4]
            mine = (t[2] + t[3] + t[4]) % big_prime
        
        if c == '0':
            t = zero, 0, 0, 0, 0
        
        if c == '1':
            t = 0, one_used, one_unused, 0, 0
        
        if c == '2':
            t = 0, 0, 0, two, 0
        
        if c == '*':
            t = 0, 0, 0, 0, mine
        
        if c == '?':
            t = zero, one_used, one_unused, two, mine
        
    #State of the program after the  for loop has been executed: `s` is a string of length `n` (1 ≤ n ≤ 10^6) consisting of characters "*", "?", and digits "0", "1", or "2"; `line` is the input string `s` and must be non-empty; `big_prime` is 1000000007; `t` is a tuple where each element represents the count of valid sequences ending in a specific pattern, modulo `big_prime`. Specifically, `t[0]` is the count of sequences ending in "0", `t[1]` is the count of sequences ending in "1" that have been used, `t[2]` is the count of sequences ending in "1" that have not been used, `t[3]` is the count of sequences ending in "2", and `t[4]` is the count of sequences ending in "*". If `s` is empty, `t` remains `None`.
    print(t[0] + t[1] + t[4]) % big_prime
#Overall this is what the function does:The function processes a string `s` of length `n` (1 ≤ n ≤ 10^6) consisting of characters "*", "?", and digits "0", "1", or "2". It calculates the number of valid sequences that can be formed by interpreting these characters, where each sequence ends in a specific pattern, and the counts are taken modulo 1000000007. The function prints the total count of valid sequences ending in "0", "1" (used), or "*". The function does not return any value; instead, it prints the result directly. If the input string `s` is empty, the function will print 0.

