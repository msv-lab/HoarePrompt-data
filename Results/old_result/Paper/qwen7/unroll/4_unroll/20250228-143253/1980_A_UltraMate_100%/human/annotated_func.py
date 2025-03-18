#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5; a is a string of length n consisting of characters from 'A' to 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEFG'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: t is the number of test cases, and for each test case, t is an integer between 1 and 1000. For each test case, n and m are integers, s is a string consisting of uppercase letters from 'A' to 'G', and ans is the calculated value based on the conditions given in the loop. The final output is the value of ans for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `t` (number of test cases), two integers `n` and `m`, and a string `s` of length `n` containing characters from 'A' to 'G'. For each test case, it calculates and prints the value of `ans`, which is determined based on the counts of characters in `s` compared to the integer `m`. Specifically, `ans` is incremented by `m` for each character in 'ABCDEFG' that is not present in `s`, and for each character present in `s`, `ans` is incremented by the difference between `m` and the count of that character in `s`.

