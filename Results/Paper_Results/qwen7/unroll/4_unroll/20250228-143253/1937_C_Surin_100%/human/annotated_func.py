#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. The interactor provides a fixed permutation p_0, p_1, ..., p_{n-1} which is a permutation of {0, 1, ..., n-1}.
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
        
    #State: Output State: The value of `prev` and `v1` are determined based on the comparisons made within the loop. Specifically, `v1` will hold the value that was compared with `prev` in the last iteration where `r` was either `<` or `=`. The value of `prev` will be the last position where the comparison resulted in `>` or `=`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it determines two specific values, `prev` and `v1`, through a series of comparisons. It prints a sequence of queries to compare elements in a given permutation and updates `v1` and `prev` based on the comparison results. After processing all test cases, it outputs the final values of `prev` and `v1`.

