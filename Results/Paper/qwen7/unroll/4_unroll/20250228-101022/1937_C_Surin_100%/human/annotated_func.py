#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. The interactor chooses a fixed permutation p_0, p_1, ..., p_{n-1} which is a permutation of {0, 1, ..., n-1}.
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
        
    #State: Output State: The output state will consist of two integers separated by a space. The first integer represents the value of `prev` after all iterations, and the second integer represents the value of `v1` after all iterations. These values are determined based on the comparisons made within the loop and the responses received from the input.
    #
    #In the loop, `v1` is updated when the response is '<', and `prev` is updated when the response is '>'. If both `v1` and `prev` are equal at any point, the loop continues until the final comparison where the value of `prev` and `v1` are printed as the output.
#Overall this is what the function does:The function performs a series of queries to determine the relative order of elements in an unknown permutation of numbers from 0 to n-1. It iteratively updates two variables, `v1` and `prev`, based on the responses received from these queries. After completing the iterations, it prints the final values of `prev` and `v1`. The function does not accept any parameters and returns no value.

