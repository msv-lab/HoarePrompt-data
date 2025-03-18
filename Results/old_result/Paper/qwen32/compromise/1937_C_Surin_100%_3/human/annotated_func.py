#State of the program right berfore the function call: There are multiple test cases, each with an integer n (2 ≤ n ≤ 10⁴) representing the length of a permutation p of {0, 1, ..., n-1}. For each test case, the function can make at most 3n queries to compare bitwise OR operations on pairs of elements in p, and must identify a pair of indices i and j such that p_i ⊕ p_j is maximized.
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
        
    #State: kp is the total number of test cases minus one, n is the input integer for the current test case, g is 0, v1 is the index of the element in the permutation that, when XORed with another element, yields the maximum possible value, i is n-1, v2 is n-1, prev is the index of the element that, when XORed with the element at index v1, yields the maximum possible value.
#Overall this is what the function does:The function processes multiple test cases, each involving a permutation of integers from 0 to n-1. It uses a limited number of queries to determine a pair of indices such that the bitwise XOR of the elements at these indices is maximized. The function outputs the indices of this pair for each test case.

