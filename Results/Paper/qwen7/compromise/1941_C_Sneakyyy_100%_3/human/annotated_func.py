#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of all n across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = input()
        
        ans = 0
        
        i = 0
        
        while i < len(a) - 2:
            s = a[i:i + 3]
            if s == 'map' or s == 'pie':
                i += 3
                ans += 1
            else:
                i += 1
        
        print(ans)
        
    #State: Output State: After the loop executes all its iterations, the final state will be:
    #
    #- `i` will be equal to `len(a) - 2`, as the loop continues to increment `i` until it reaches this value.
    #- `ans` will contain the total count of occurrences where the substring `s` (of length 3) starting from index `i` is either 'map' or 'pie'.
    #- `t` will remain a positive integer such that \(1 \leq t \leq 10^4\), as it is not affected by the loop.
    #- `n` will remain an input integer, unchanged by the loop.
    #- `a` will remain unchanged as it is not modified within the loop.
    #- `s` will be the substring of `a` starting from the index `len(a) - 2` and having a length of 3 (unless the index `len(a)` is out of bounds, in which case `s` will be shorter or non-existent).
    #
    #In summary, the loop processes all possible substrings of length 3 in the string `a`, counting how many times the substrings 'map' or 'pie' appear, and sets `i` to the position just before the last possible substring of length 3. The other variables retain their initial values.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` (1 ≤ t ≤ 10^4), a positive integer `n` (1 ≤ n ≤ 10^6), and a string `s` of length `n` consisting of lowercase Latin letters. For each test case, it counts the number of occurrences of the substrings 'map' and 'pie' in the string `s`. The function then prints the total count of these occurrences for each test case.

