#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. The string s is a string of length m comprising only the first k lowercase English alphabets. It is guaranteed that the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: Output State: `ps` is the number of times a substring of length `k` containing only characters from the set `us` was found in the string `s`, `t` remains unchanged, `n` remains unchanged, `k` remains unchanged, `m` remains unchanged, `s` remains unchanged, `us` is a set containing the first `k` lowercase letters starting from 'a', `win` is an empty set, `ans` is a list containing the last character of each valid substring of length `k` found in `s`.
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES'
    #State: `ps` is the number of times a substring of length `k` containing only characters from the set `us` was found in the string `s`, `t` remains unchanged, `n` remains unchanged, `k` remains unchanged, `m` remains unchanged, `s` remains unchanged, `us` is a set containing the first `k` lowercase letters starting from 'a', `win` is an empty set, `ans` is a list containing the last character of each valid substring of length `k` found in `s`, and `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: Output State: `ps` is the number of times a substring of length `k` containing only characters from the set `us` was found in the string `s`, `t` remains unchanged, `n` remains unchanged, `k` remains unchanged, `m` remains unchanged, `s` remains unchanged, `us` is a set containing the first `k` lowercase letters starting from 'a', `win` is a set containing the first `k` lowercase letters starting from 'a', `ans` is a list containing the last character of each valid substring of length `k` found in `s`, and `ps` is less than `n`.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers \(n\), \(k\), and \(m\), and a string \(s\) of length \(m\) consisting of the first \(k\) lowercase English alphabets. It checks if there are at least \(n\) substrings of length \(k\) within \(s\) that contain only characters from the first \(k\) lowercase English alphabets. If such substrings are found, it prints 'YES'. Otherwise, it determines and prints a specific character sequence based on the remaining characters needed to meet the condition.

