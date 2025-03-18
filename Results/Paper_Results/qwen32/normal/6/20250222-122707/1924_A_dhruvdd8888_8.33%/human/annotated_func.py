#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n, k, and m are integers such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000. s is a string of length m consisting only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^5; `n`, `k`, and `m` are integers read from the input such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000; `s` is a string of length `m` consisting only of the first `k` lowercase English alphabets; `us` is a set containing the first `k` lowercase English alphabets; `win` is an empty set; `ans` is a list containing characters from `s` that caused `win` to reach its size of `k`; `ps` is the number of times `win` reached its size of `k`.
    if (ps >= n) :
        return print('YES')
        #The program returns print('YES')
    #State: `t` is an integer such that 1 <= t <= 10^5; `n`, `k`, and `m` are integers read from the input such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000; `s` is a string of length `m` consisting only of the first `k` lowercase English alphabets; `us` is a set containing the first `k` lowercase English alphabets; `win` is an empty set; `ans` is a list containing characters from `s` that caused `win` to reach its size of `k`; `ps` is a number of times `win` reached its size of `k`, and `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: `t` is an integer such that 1 <= t <= 10^5; `n`, `k`, and `m` are integers read from the input such that 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000; `s` is a string of length `m` consisting only of the first `k` lowercase English alphabets; `us` is a set containing the first `k` lowercase English alphabets; `win` is a set containing all `k` elements from `us`; `ans` is a list containing characters from `s` that caused `win` to reach its size of `k`; `ps` is a number of times `win` reached its size of `k`, and `ps` is less than `n`.
#Overall this is what the function does:The function reads integers `n`, `k`, and `m`, and a string `s` from the input. It checks if it's possible to find at least `n` distinct sequences in `s` where each sequence contains all `k` unique lowercase English alphabets. If such sequences exist, it prints 'YES'. If not, it prints 'NO' and then for each missing alphabet in the last sequence, it prints a constructed string that includes the found sequences, the missing alphabet, and additional 'a's to meet the required sequence length of `n`.

