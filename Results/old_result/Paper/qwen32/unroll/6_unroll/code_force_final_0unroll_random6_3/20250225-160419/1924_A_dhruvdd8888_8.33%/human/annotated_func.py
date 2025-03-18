#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26, and m is an integer such that 1 <= m <= 1000. The string s is of length m and consists only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: win is an empty set; ans is a list containing the last character of each sequence of k distinct characters found in s; ps is the number of such sequences found.
    if (ps >= n) :
        return print('YES')
        #The program prints 'YES'
    #State: win is an empty set; ans is a list containing the last character of each sequence of k distinct characters found in s; ps is the number of such sequences found, and ps is less than n
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: win is a set containing all unique characters from `us` that were printed; ans is unchanged; ps is unchanged.
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n`, `k`, `m`, and a string `s`. For each test case, it checks if there are at least `n` sequences of `k` distinct characters in the string `s`. If such sequences exist, it prints 'YES'. If not, it prints 'NO' and then, for each missing sequence, it prints a constructed string that includes the last characters of found sequences, a missing character from the set of the first `k` lowercase English alphabets, and padding with 'a' to meet the length requirement of `n`.

