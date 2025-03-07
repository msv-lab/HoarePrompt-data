#State of the program right berfore the function call: The function operates in an interactive environment with a secret permutation p of integers from 0 to n-1, where n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to compare bitwise OR results of pairs of elements from the permutation. The function must find and output a pair of indices (i, j) such that p_i ⊕ p_j is maximized, and 0 ≤ i, j < n. The total sum of n over all test cases does not exceed 10^4.
def func():
    I = lambda : list(map(int, input().split(' ')))
    R = lambda : int(input())
    for kp in range(int(input())):
        n = int(input())
        
        g = 0
        
        v1 = 0
        
        for i in range(1, n):
            v2 = i
            print(f'? {v1} {v1} {v2} {v2}')
            sys.stdout.flush()
            r = input('')
            if r == '<':
                v1 = v2
        
        prev = 0
        
        for i in range(1, n):
            print(f'? {v1} {i} {v1} {prev}')
            sys.stdout.flush()
            r = input()
            if r == '>':
                prev = i
            elif r == '=':
                print(f'? {i} {i} {prev} {prev}')
                sys.stdout.flush()
                r2 = input('')
                if r2 == '<':
                    prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: For each iteration of the loop, the output state after the loop finishes is that the pair of indices (prev, v1) is printed such that p_prev ⊕ p_v1 is maximized for the given permutation p of integers from 0 to n-1. The loop iterates kp times, and for each iteration, the variables n, g, v1, and prev are reset and updated according to the logic of the loop. After all iterations, the final state of these variables is not defined as they are reset at the start of each new iteration.
#Overall this is what the function does:The function `func` operates in an environment with a secret permutation `p` of integers from 0 to n-1, where 2 ≤ n ≤ 10^4. It processes `kp` test cases, each with a different value of `n`. For each test case, the function makes at most 3n queries to compare bitwise OR results of pairs of elements from the permutation. It then outputs a pair of indices `(prev, v1)` such that the bitwise XOR of `p[prev]` and `p[v1]` is maximized, with 0 ≤ prev, v1 < n. After processing all test cases, the function does not retain any state from previous iterations.

