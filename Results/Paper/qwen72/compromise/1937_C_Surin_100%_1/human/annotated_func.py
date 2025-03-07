#State of the program right berfore the function call: The function operates within an interactive environment where a secret permutation p of integers from 0 to n-1 is provided, and the function can make at most 3n queries to find the indices i and j such that p_i ⊕ p_j is maximized. The input n is a positive integer (2 ≤ n ≤ 10^4), and the total number of test cases t is a positive integer (1 ≤ t ≤ 10^3) with the sum of n over all test cases not exceeding 10^4.
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
        
    #State: The loop will have executed `t` times, where `t` is the number of test cases. For each test case, the variables `n`, `g`, `v1`, and `prev` will have been updated as follows: `n` will be the input integer for that test case, `g` will remain 0, `v1` will be the largest integer in the range [1, n-1] such that the response from the input is '<', and `prev` will be the integer that satisfies the conditions of the second and third queries in the loop. After all iterations, the loop will have printed the result `! {prev} {v1}` for each test case.
#Overall this is what the function does:The function `func` operates within an interactive environment to solve multiple test cases. For each test case, it takes an integer `n` (2 ≤ n ≤ 10^4) as input and makes at most 3n queries to find and print two indices `prev` and `v1` such that the bitwise XOR of the elements at these indices in a secret permutation `p` of integers from 0 to n-1 is maximized. After processing all test cases, the function ensures that the sum of `n` over all test cases does not exceed 10^4. The function does not return any value but prints the results in the format `! {prev} {v1}` for each test case.

