#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³, and for each test case, n is an integer such that 2 ≤ n ≤ 10⁴. The sum of n over all test cases does not exceed 10⁴.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: t is an integer such that 1 ≤ t ≤ 10³; n is the input integer for the last test case; k is the largest index i (from 2 to n-1) for which the response was '<' in the last test case, or 1 if no such response was received; best is the largest index i (from 1 to n-1) for which the response was '<' in the last test case, or 0 if no such response was received; res is the value of the user's input for the last iteration of the second inner loop in the last test case; i is n-1.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` (where 2 ≤ n ≤ 10⁴). For each test case, it interacts with an external process by sending queries and receiving responses to determine two specific indices, `k` and `best`, and then outputs these indices. The final state of the program after processing all test cases is that it has output the determined indices for each test case.

