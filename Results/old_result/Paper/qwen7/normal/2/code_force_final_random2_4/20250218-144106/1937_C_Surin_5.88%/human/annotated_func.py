#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem description indicates that the interaction involves querying indices and comparing results based on bitwise operations. The variables n, a, b, c, d, x, y, and the permutation p are implicitly involved in the interaction process but are not passed as arguments to the function.
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
        
    #State: i is n, n is the input integer, r is the input string, g is 0, v1 is n - 1, v2 is n - 1, and prev is n - 1 or any value between 1 and n-1 inclusive, depending on the user's inputs ('>') during each iteration.
#Overall this is what the function does:The function interacts with the user to determine the values of `prev` and `v1` based on comparisons using indices. It prints queries to the user, receives responses, and updates `prev` and `v1` accordingly. After completing the interactions, it outputs the final values of `prev` and `v1`.

