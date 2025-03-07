#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5, and a is a string of length n consisting of characters from 'A' to 'G'.
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
        
    #State: Output State: The final value of `ans` will be the total sum calculated based on the conditions provided within the loop, considering all inputs given during each iteration of the loop.
    #
    #To explain further, after all iterations of the loop have finished, `ans` will be the cumulative sum of `m - hmp[i]` for all unique characters in the string `s` (as provided in each iteration) where `hmp[i]` is less than `m`. If a character does not appear in the string `s` at all, it contributes `m` to `ans`. This calculation happens for every string `s` provided in each iteration of the loop, with `m` being the value of `m` from the last iteration since it is not redefined inside the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \(t\), \(n\), and \(m\), and a string \(a\) of length \(n\) containing characters from 'A' to 'G'. For each test case, it calculates the total sum of \(m - \text{count}(i)\) for all unique characters \(i\) in the string \(a\), where \(\text{count}(i)\) is the number of occurrences of character \(i\) in the string \(a\). If a character does not appear in the string \(a\), it adds \(m\) to the total sum. The final output is the cumulative sum of these calculations across all test cases.

