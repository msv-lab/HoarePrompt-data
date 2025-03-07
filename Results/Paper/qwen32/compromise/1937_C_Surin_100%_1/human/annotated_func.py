#State of the program right berfore the function call: There are multiple test cases, each containing a permutation p of integers from 0 to n-1, where 2 ≤ n ≤ 10^4. The sum of n over all test cases does not exceed 10^4. For each test case, the function can ask at most 3n queries in the form "? a b c d" to compare the bitwise OR of pairs (p_a, p_b) and (p_c, p_d). After determining the indices i and j that maximize p_i \oplus p_j, the function should output "! i j".
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
        
    #State: `kp` is equal to the total number of test cases, `n` is the integer input for the last test case, `g` is 0, `v1` is the largest integer `i` (from 1 to `n-1`) for which the user's response was `'<'` during the last test case, and `prev` is the largest integer `i` (from 1 to `n-1`) for which the user's response was `'>'` or `'='` followed by `'<'` during the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a permutation of integers from 0 to n-1. For each test case, it interacts with an external system by asking up to 3n queries to compare the bitwise OR of specific pairs of elements. Based on the responses, it identifies and outputs the indices of the two elements that maximize their bitwise XOR.

