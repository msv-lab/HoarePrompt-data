#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p_0, p_1, ..., p_{n-1} of the set {0, 1, ..., n-1}. The function can interact with the interactor by making queries in the form "? a b c d" (where 0 ≤ a, b, c, d < n) and receiving a response of "<", "=", or ">" based on the comparison of (p_a | p_b) and (p_c | p_d). The function must find a pair of indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized and print "! i j" for each test case. The total number of queries across all test cases must not exceed 3n, where n is the sum of lengths of all permutations.
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
        
    #State: The loop finds and prints the two largest unique elements in the list of integers provided by the input. The variable `prev` holds the value of the second largest element, and `v1` holds the value of the largest element. All other variables (`kp`, `n`, `g`, `v2`, `r`, `r2`) are not guaranteed to retain specific values after the loop completes as they are used for intermediate calculations and comparisons. The lambda function `R` remains unchanged and is still a function that reads a line of input, splits it by spaces, converts each split string to an integer, and returns the resulting list of integers.
#Overall this is what the function does:The function processes multiple test cases, each involving a permutation of integers from 0 to n-1. For each test case, it interacts with an interactor to determine a pair of indices (i, j) that maximizes the bitwise XOR of the elements at those indices, and then prints "! i j". The function ensures that the total number of queries made across all test cases does not exceed 3n, where n is the sum of the lengths of all permutations.

