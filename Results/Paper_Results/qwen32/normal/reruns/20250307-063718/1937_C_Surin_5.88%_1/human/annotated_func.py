#State of the program right berfore the function call: There are multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p of the set {0, 1, ..., n-1}. For each test case, the function can interactively ask up to 3n queries of the form "? a b c d" to compare bitwise OR operations on elements of p, and must eventually output "! i j" to identify a pair of indices i and j that maximize the bitwise XOR of p_i and p_j. The sum of n across all test cases does not exceed 10^4.
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
        
    #State: kp is equal to the total number of test cases minus one, the number of test cases is determined by `int(input())`, `n` is the length of the permutation `p` for the current test case, `g` is 0, `v1` is the index of the element in `p` that has the highest value, `v2` is `n-1` from the last iteration of the inner loop, `prev` is the index of the element in `p` that, when XORed with `p[v1]`, gives the maximum value, `r` is the last response received, `i` is `n-1` from the last iteration of the inner loop.
#Overall this is what the function does:The function interacts with the user to determine a pair of indices in a permutation of integers that maximize the bitwise XOR of the elements at those indices. It outputs the pair of indices in the format "! i j" for each test case.

