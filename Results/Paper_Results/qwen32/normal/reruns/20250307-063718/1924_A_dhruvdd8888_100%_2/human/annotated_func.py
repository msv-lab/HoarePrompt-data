#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26. m is an integer such that 1 <= m <= 1000. s is a string of length m consisting only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: `win` is an empty set, `ans` is a list containing characters that caused `win` to be filled with `k` unique characters, and `ps` is the number of times `win` was filled with `k` unique characters.
    if (ps >= n) :
        return print('YES')
        #The program returns 'YES'
    #State: `win` is an empty set, `ans` is a list containing characters that caused `win` to be filled with `k` unique characters, and `ps` is the number of times `win` was filled with `k` unique characters. Additionally, `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: the string formed by `''.join(ans) + i + 'a' * (n - len(ans) - 1)` during the second iteration.
#Overall this is what the function does:The function reads input values for `n`, `k`, `m`, and `s`, then processes the string `s` to determine if it contains at least `n` sequences of `k` unique characters. If it does, it returns 'YES'. Otherwise, it constructs and returns a string based on the characters found in `s` and the set of the first `k` lowercase English alphabets, ensuring the string is of length `n`.

