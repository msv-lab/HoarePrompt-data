#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5. It is guaranteed that for each test case, there exists a suitable string s consisting of lowercase Latin letters a-z that corresponds to the given trace a.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: - After all test cases are processed, the variables `t`, `n`, `a`, and `b` will be in their final states.
    #   - `t` will be 0 since the loop has finished all iterations.
    #   - `n` will be the value of `n` from the last test case.
    #   - `a` will remain 'abcdefghijklmnopqrstuvwxyz'.
    #   - `b` will contain the counts of each letter used across all test cases.
    #
    #Since the problem asks for the state after all executions of the loop, we need to consider the final state of the variables after the loop has completed all iterations.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases. For each test case, it constructs and prints a string of lowercase Latin letters based on a given list of integers. Each integer in the list corresponds to a letter in the alphabet, and the function ensures that the letters are chosen such that the sequence matches the provided trace. After processing all test cases, the function does not return any value but outputs the constructed strings for each test case.

