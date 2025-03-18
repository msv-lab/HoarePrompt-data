#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. The string s is a string of length m comprising only the first k lowercase English alphabets. Additionally, the sum of m and the sum of n over all test cases does not exceed 10^6.
def func_1():
    n, k, m = tuple(map(int, input().split()))
    s = input()
    us = set(chr(i + 97) for i in range(k))
    win = set()
    ans = []
    ps = 0
    for i in s:
        if i in us:
            win.add(i)
            if len(win) == k:
                ans.append(i)
                ps += 1
                win.clear()
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^5, `n` is an integer such that 1 ≤ n ≤ 26, `k` is an integer such that 1 ≤ k ≤ 26, `m` is an integer such that 1 ≤ m ≤ 1000, `s` is a string input by the user, `us` is a set containing the first `k` lowercase letters of the alphabet, `win` is a set containing the last `k` unique characters from `s` that are in `us`, `ans` is a list containing the last character added to `win` for each group of `k` unique characters from `s` that are in `us`, `ps` is an integer equal to the number of times `win` was cleared.
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES'
    #State: `t` is an integer such that 1 ≤ t ≤ 10^5, `n` is an integer such that 1 ≤ n ≤ 26, `k` is an integer such that 1 ≤ k ≤ 26, `m` is an integer such that 1 ≤ m ≤ 1000, `s` is a string input by the user, `us` is a set containing the first `k` lowercase letters of the alphabet, `win` is a set containing the last `k` unique characters from `s` that are in `us`, `ans` is a list containing the last character added to `win` for each group of `k` unique characters from `s` that are in `us`, `ps` is an integer less than `n` equal to the number of times `win` was cleared.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^5, `n` is an integer such that 1 ≤ n ≤ 26, `k` is an integer such that 1 ≤ k ≤ 26, `m` is an integer such that 1 ≤ m ≤ 1000, `s` is a string input by the user, `us` is a set containing the first `k` lowercase letters of the alphabet, `win` is a set containing the last `k` unique characters from `s` that are in `us`, `ans` is a list containing the last character added to `win` for each group of `k` unique characters from `s` that are in `us`, `ps` is an integer less than `n` equal to the number of times `win` was cleared, `i` is a character from the first `k` lowercase letters of the alphabet that is not in `win`.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers \( n \), \( k \), and \( m \), and a string \( s \). It checks if the string \( s \) contains at least \( n \) distinct characters from the first \( k \) lowercase English alphabets. If any test case meets this criterion, the function prints 'YES'. Otherwise, it determines which character from the first \( k \) lowercase English alphabets is missing and prints a string consisting of the characters in the list \( ans \) followed by the missing character and the remaining characters needed to satisfy the count \( n \). If none of the test cases meet the criterion, the function prints 'NO'.

