#State of the program right berfore the function call: None of the input variables are explicitly defined in the function signature. However, the problem description implies that the function interacts with an external entity (the interactor) through standard input and output. The interactor provides the number of test cases and the details of each test case, including the size of the permutation and the results of the queries. The function must manage up to 3n queries for each test case and handle the responses accordingly.
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
    #In the loop, `v1` is updated when the response to the query is '<', and `prev` is updated when the response to the query is '>'. If the response is '=', a further check is made to ensure `prev` is updated correctly. The final output is '! prev v1'.
#Overall this is what the function does:The function interacts with an external interactor through standard input and output. It processes multiple test cases, where for each test case, it determines the position of a specific element in a permutation based on comparison queries. For each test case, it makes up to 3n queries to the interactor and updates variables `v1` and `prev` based on the responses. After processing all queries for a test case, it outputs the final positions of `prev` and `v1`.

