#State of the program right berfore the function call: The function operates within an interactive environment where it interacts with a hidden permutation p of integers from 0 to n-1, and it must find two indices i and j such that p_i ⊕ p_j is maximized using at most 3n queries. The function receives input through a series of queries and outputs the result of the queries and the final answer in a specific format. The number of test cases t is an integer where 1 ≤ t ≤ 10^3, and for each test case, n is an integer where 2 ≤ n ≤ 10^4. The total sum of n across all test cases does not exceed 10^4.
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
        
    #State: After the loop completes all its iterations, `kp` is `t-1` (where `t` is the total number of test cases), `n` is the last input integer for the final test case, `g` is 0, `v1` is the last value of `i` where the input was `<` for the final test case, or 0 if no input was `<`, `i` is `n-1` for the final test case, and `prev` is the last value of `i` where the input was `>` for the final test case, or 0 if no input was `>`.
#Overall this is what the function does:The function `func` operates in an interactive environment to solve a problem involving a hidden permutation `p` of integers from 0 to n-1. It processes multiple test cases, each defined by an integer `n` (2 ≤ n ≤ 10^4), with the total sum of `n` across all test cases not exceeding 10^4. For each test case, the function finds two indices `i` and `j` such that the XOR of `p[i]` and `p[j]` is maximized, using at most 3n queries. The function outputs the results of these queries and the final answer in a specific format, printing the indices `i` and `j` in the form `! i j`. After processing all test cases, the function terminates without returning any value.

