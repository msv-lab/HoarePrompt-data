#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem description implies that the function should interact with an external entity to perform queries and receive responses. The variables n, a, b, c, d, x, y, and the permutation p are not part of the function's parameters but are used in the interaction process.
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
        
    #State: Output State: The output state will consist of two integers separated by a space. The first integer represents the value of `prev` after the loop completes, and the second integer represents the value of `v1` after the loop completes. These values are determined by the comparisons made within the loop based on the user's input ('<' or '>').
    #
    #In each iteration of the loop, `v1` is updated to `v2` if the user inputs '<', and `prev` is updated to `i` if the user inputs '>'. The final values of `prev` and `v1` after all iterations represent the output state.
#Overall this is what the function does:The function interacts with an external entity to perform queries and receives responses. It iterates through a sequence of comparisons based on the user's input ('<' or '>'), updating two variables `prev` and `v1` accordingly. After completing the iterations, it outputs two integers separated by a space, where the first integer is the final value of `prev` and the second integer is the final value of `v1`.

