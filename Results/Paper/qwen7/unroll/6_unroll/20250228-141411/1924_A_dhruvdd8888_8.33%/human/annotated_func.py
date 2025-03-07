#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26, and m is an integer such that 1 ≤ m ≤ 1000. Additionally, s is a string of length m comprising only the first k lowercase English alphabets. It is guaranteed that the sum of m and the sum of n over all test cases does not exceed 10^6.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^5, `n` is an integer such that 1 ≤ n ≤ 26, `k` is an integer such that 1 ≤ k ≤ 26, `m` is an integer such that 1 ≤ m ≤ 1000, `s` is a string input by the user; `us` is a set containing the first `k` lowercase letters of the alphabet; `win` is a set that may contain up to `k` lowercase letters from the string `s`; `ans` is a list that contains the last `k` unique characters from `s` that are also in `us`, each repeated once for each time they were the `k`th unique character encountered; `ps` is an integer representing the number of times a set of `k` unique characters was fully collected from `s`.
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES'
    #State: `t` is an integer such that 1 ≤ t ≤ 10^5, `n` is an integer such that 1 ≤ n ≤ 26, `k` is an integer such that 1 ≤ k ≤ 26, `m` is an integer such that 1 ≤ m ≤ 1000, `s` is a string input by the user; `us` is a set containing the first `k` lowercase letters of the alphabet; `win` is a set that may contain up to `k` lowercase letters from the string `s`; `ans` is a list that contains the last `k` unique characters from `s` that are also in `us`, each repeated once for each time they were the `k`th unique character encountered; `ps` is an integer representing the number of times a set of `k` unique characters was fully collected from `s`. The value of `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^5, `n` is an integer such that 1 ≤ n ≤ 26, `k` is an integer such that 1 ≤ k ≤ 26, `m` is an integer such that 1 ≤ m ≤ 1000, `s` is a string input by the user; `us` is a set containing the first `k` lowercase letters of the alphabet; `win` is a set that may contain up to `k` lowercase letters from the string `s`; `ans` is a list that contains the last `k` unique characters from `s` that are also in `us`, each repeated once for each time they were the `k`th unique character encountered; `ps` is an integer representing the number of times a set of `k` unique characters was fully collected from `s`, incremented by the number of times the loop executed; `i` is the last character printed in the loop, which is one of the first `k` lowercase letters of the alphabet.
#Overall this is what the function does:The function processes a string `s` and checks if it contains at least `n` sets of the first `k` unique lowercase English alphabets. If it finds at least `n` such sets, it prints 'YES'. Otherwise, it prints 'NO' and then outputs a specific string based on the missing characters.

