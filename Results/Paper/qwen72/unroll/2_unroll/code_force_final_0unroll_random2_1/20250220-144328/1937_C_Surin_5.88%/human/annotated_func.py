#State of the program right berfore the function call: The function operates in an interactive environment where the input is provided through queries and responses. The input includes multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p of integers from 0 to n-1. The function can make at most 3n queries to find indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized. The total sum of n over all test cases does not exceed 10^4.
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
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: The loop will execute `kp` times, where `kp` is the number of test cases provided. For each test case, the loop will find the maximum value `prev` and the value `v1` which is the largest number less than `n` such that all pairs `(v1, i)` where `i` ranges from 1 to `n-1` satisfy the condition `v1 > i`. The final output for each test case will be `! {prev} {v1}`, where `prev` is the largest value less than `v1` that satisfies the condition `v1 > i`. After all iterations, the values of `kp`, `n`, `g`, `v1`, and `prev` will be reset for each new test case, but the number of test cases `kp` will be exhausted.
#Overall this is what the function does:The function operates in an interactive environment to process multiple test cases. For each test case, it finds and outputs two indices `i` and `j` from a permutation `p` of integers from 0 to n-1, such that the XOR of `p_i` and `p_j` is maximized. The function makes at most 3n queries to the environment to determine these indices. After processing all test cases, the function has no return value but has printed the results for each test case in the format `! {prev} {v1}`, where `prev` and `v1` are the indices found.

