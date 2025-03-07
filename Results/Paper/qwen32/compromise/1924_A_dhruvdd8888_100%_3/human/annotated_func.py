#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26. m is an integer such that 1 <= m <= 1000. s is a string of length m consisting only of the first k lowercase English alphabets. The sum of m over all test cases does not exceed 10^6. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: `win` is an empty set; `ans` is a list containing the last character of each sequence of `k` distinct characters found in `s`; `ps` is the count of such sequences.
    if (ps >= n) :
        return print('YES')
        #The program returns None because print('YES') outputs 'YES' to the console but does not return any value.
    #State: `win` is an empty set; `ans` is a list containing the last character of each sequence of `k` distinct characters found in `s`; `ps` is the count of such sequences, and `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: xybaa
#Overall this is what the function does:The function reads input values for `n`, `k`, `m`, and a string `s`, then checks if there are at least `n` sequences of `k` distinct characters in `s`. If there are, it prints 'YES'. Otherwise, it prints 'NO' and, if applicable, constructs and prints a string of length `n` using characters from the first `k` lowercase English alphabets, ensuring it includes the last characters of found sequences and additional characters to meet the length requirement.

