#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^5), representing the number of test cases. Each element in cases is a tuple (n, k, m, s) where n is a positive integer (1 ≤ n ≤ 26), k is a positive integer (1 ≤ k ≤ 26), m is a positive integer (1 ≤ m ≤ 1000), and s is a string of length m comprising only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: `t` remains a positive integer (1 ≤ t ≤ 10^5), `cases` remains unchanged, `s` is updated to the input string, `us` remains a set containing the first `k` lowercase English alphabets, `win` is an empty set, `ans` is a list containing the characters that were added when the set `win` had all `k` unique characters, and `ps` is the number of times the set `win` was cleared (i.e., the number of times all `k` unique characters were found in a contiguous subsequence of `s`).
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES' and returns it.
    #State: `t` remains a positive integer (1 ≤ t ≤ 10^5), `cases` remains unchanged, `s` is updated to the input string, `us` remains a set containing the first `k` lowercase English alphabets, `win` is an empty set, `ans` is a list containing the characters that were added when the set `win` had all `k` unique characters, and `ps` is the number of times the set `win` was cleared (i.e., the number of times all `k` unique characters were found in a contiguous subsequence of `s`). Additionally, `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: The loop does not execute fully because it returns in the first iteration where `i` is not in `win`. The variable `ans` remains unchanged, `win` remains an empty set, and `ps` remains unchanged. The loop returns a string that is the concatenation of `ans`, the first character `i` from `us` that is not in `win`, and `n - len(ans) - 1` 'a' characters.
#Overall this is what the function does:The function `func_1` reads two lines of input: the first line contains three integers `n`, `k`, and `m`, and the second line contains a string `s` of length `m`. It processes the string `s` to find contiguous subsequences of `k` unique characters. If the number of such subsequences found is greater than or equal to `n`, the function prints 'YES' and returns 'YES'. If fewer than `n` such subsequences are found, the function prints 'NO' and returns a string that is the concatenation of the characters found in the subsequences, the first character from the set of the first `k` lowercase English alphabets that is not in the last subsequence, and `n - len(ans) - 1` 'a' characters.

