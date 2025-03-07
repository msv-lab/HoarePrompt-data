#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^5. For each test case, n, k, and m are integers such that 1 ≤ n ≤ 26, 1 ≤ k ≤ 26, and 1 ≤ m ≤ 1000. s is a string of length m consisting of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^5; `n`, `k`, and `m` are integers read from the input such that 1 ≤ n ≤ 26, 1 ≤ k ≤ 26, and 1 ≤ m ≤ 1000; `s` is a string of length m consisting of the first k lowercase English alphabets read from the input; `us` is a set containing the first `k` lowercase English alphabets; `win` is an empty set; `ans` is a list containing the last character of each sequence of `k` distinct characters found in `s`; `ps` is the number of such sequences found in `s`.
    if (ps >= n) :
        return print('YES')
        #The program returns print('YES')
    #State: `t` is an integer such that 1 ≤ t ≤ 10^5; `n`, `k`, and `m` are integers read from the input such that 1 ≤ n ≤ 26, 1 ≤ k ≤ 26, and 1 ≤ m ≤ 1000; `s` is a string of length m consisting of the first k lowercase English alphabets read from the input; `us` is a set containing the first `k` lowercase English alphabets; `win` is an empty set; `ans` is a list containing the last character of each sequence of `k` distinct characters found in `s`; `ps` is the number of such sequences found in `s` and `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: t is an integer such that 1 ≤ t ≤ 10^5, n, k, and m are integers read from the input such that 1 ≤ n ≤ 26, 1 ≤ k ≤ 26, and 1 ≤ m ≤ 1000, s is a string of length m consisting of the first k lowercase English alphabets read from the input, us is a set containing the first k lowercase English alphabets, win is a set containing all characters from us, ans is a list containing the last character of each sequence of k distinct characters found in s, and ps is the number of such sequences found in s and ps is less than n.
#Overall this is what the function does:The function reads input values `n`, `k`, and `m`, followed by a string `s`. It checks if there are at least `n` sequences of `k` distinct characters in `s`. If so, it prints 'YES'. If not, it prints 'NO' and then constructs and prints a string of length `n` using the characters found in `s` and additional characters from the first `k` lowercase English alphabets to meet the requirement.

