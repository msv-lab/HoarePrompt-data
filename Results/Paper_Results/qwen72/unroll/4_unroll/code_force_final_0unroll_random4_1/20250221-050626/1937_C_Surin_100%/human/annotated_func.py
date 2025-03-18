#State of the program right berfore the function call: The function operates in an interactive environment with a hidden permutation p of integers from 0 to n-1, where n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to compare bitwise OR results of selected indices. The number of test cases t is an integer such that 1 ≤ t ≤ 10^3, and the sum of n over all test cases does not exceed 10^4.
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
        
    #State: For each test case, the loop will output two integers, `prev` and `v1`, which are indices in the permutation `p` such that `p[prev]` and `p[v1]` are the maximum and second maximum values in the permutation, respectively. The loop will complete all iterations for each test case, and the final values of `prev` and `v1` will be printed in the format `! prev v1` for each test case.
#Overall this is what the function does:The function `func` operates in an interactive environment to determine and output the indices of the maximum and second maximum values in a hidden permutation `p` of integers from 0 to n-1, where `n` is an integer such that 2 ≤ n ≤ 10^4. For each test case, the function makes at most 3n queries to compare bitwise OR results of selected indices. After processing each test case, the function outputs two integers, `prev` and `v1`, which are the indices of the maximum and second maximum values in the permutation, respectively, in the format `! prev v1`. The function processes all test cases and completes its execution.

