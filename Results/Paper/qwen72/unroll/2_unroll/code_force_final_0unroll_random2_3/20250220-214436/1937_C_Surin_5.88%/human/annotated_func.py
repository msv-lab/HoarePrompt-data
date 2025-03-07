#State of the program right berfore the function call: The function operates in an interactive environment where the input is a sequence of queries and responses. The sequence p is a permutation of {0, 1, ..., n-1} for each test case, and n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries of the form "? a b c d" where 0 ≤ a, b, c, d < n, and must output a pair of indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop will execute `kp` times, where `kp` is the integer input at the beginning. For each iteration of the loop, `n` is set to the integer input provided for that iteration. After the loop completes, `v1` will be the largest integer less than `n` for which the first query returned '<', and `prev` will be the largest integer less than `n` for which the second query returned '>'. The final output for each iteration will be `! {prev} {v1}`. The initial state of the lambda function `R` remains unchanged.
#Overall this is what the function does:The function `func` operates in an interactive environment to find and output a pair of indices (i, j) from a permutation p of {0, 1, ..., n-1} such that the XOR of p_i and p_j is maximized. The function reads an integer `kp` indicating the number of test cases. For each test case, it reads an integer `n` (2 ≤ n ≤ 10^4), performs a series of queries to determine the indices, and outputs the pair of indices (i, j) that achieve the maximum XOR value. The function does not return any value; it only prints the results to the standard output. After the function concludes, the state of the program includes the processed test cases with the corresponding pairs of indices printed.

