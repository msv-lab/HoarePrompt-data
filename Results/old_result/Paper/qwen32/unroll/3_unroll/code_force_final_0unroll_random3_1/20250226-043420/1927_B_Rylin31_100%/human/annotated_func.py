#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5. It is guaranteed that for each test case, a valid string s exists that corresponds to the given trace.
def func():
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: For each test case, the output is a string `ans` constructed by appending characters based on the values in the list `s` and the indices in `array`. The state of `t`, `n`, and the list `a` remains unchanged as they are part of the precondition and not modified within the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it generates a string by mapping each integer in `a` to a corresponding character, ensuring that each integer maps to a unique character sequence. The function outputs this string for each test case. The input values `t`, `n`, and `a` remain unchanged throughout the execution.

