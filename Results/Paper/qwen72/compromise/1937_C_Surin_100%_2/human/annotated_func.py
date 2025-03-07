#State of the program right berfore the function call: The function operates in an interactive environment where it receives input through queries and outputs indices. The input includes multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the size of a permutation of integers from 0 to n-1. The function can make at most 3n queries to compare bitwise OR results of pairs of elements in the permutation. The total sum of n over all test cases does not exceed 10^4.
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
        
    #State: After all iterations, `kp` is equal to the input integer provided at the start of the loop, `n` is the last input integer provided within the loop, `v1` is the last value of `i` where `r` was `<` or 0 if `r` was never `<`, `prev` is the last value of `i` where `r` was `>` or `=`, and the output buffer has been flushed. The loop prints the final result as `! {prev} {v1}`.
#Overall this is what the function does:The function `func` operates in an interactive environment to determine two indices, `prev` and `v1`, based on the bitwise OR results of pairs of elements in a permutation of integers from 0 to n-1, where n is an integer (2 ≤ n ≤ 10^4). The function processes multiple test cases, each with a different value of n. For each test case, it makes at most 3n queries to compare the bitwise OR results. After processing all test cases, the function prints the final result as `! {prev} {v1}` for each case, where `prev` is the last value of `i` where the comparison result was `>` or `=`, and `v1` is the last value of `i` where the comparison result was `<` or 0 if no such `i` was found. The function ensures that the output buffer is flushed after each query and the final result.

