#State of the program right berfore the function call: The function operates in an interactive environment with a hidden permutation p of integers from 0 to n-1, where n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to compare bitwise OR results of pairs of elements from the permutation. The function must output a pair of indices (i, j) such that p_i ⊕ p_j is maximized, and 0 ≤ i, j < n. The total sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop has executed all iterations, and for each permutation `p` of length `n`, the output is a pair of indices (i, j) such that `p_i ⊕ p_j` is maximized, with 0 ≤ i, j < n. The variables `kp`, `n`, `g`, `v1`, and `prev` are updated as per the loop's logic, but the hidden permutation `p` and the function definitions `I` and `R` remain unchanged.
#Overall this is what the function does:The function `func` operates in an interactive environment to find and output a pair of indices (i, j) such that the bitwise XOR of the elements at these indices in a hidden permutation `p` is maximized. The function processes multiple test cases, each with a permutation of integers from 0 to n-1, where 2 ≤ n ≤ 10^4. After processing each test case, the function outputs a pair of indices (i, j) such that `p_i ⊕ p_j` is maximized, with 0 ≤ i, j < n. The function does not return any value; it only prints the results to the standard output. The hidden permutation `p` remains unchanged, and the function definitions `I` and `R` are not used in the function.

