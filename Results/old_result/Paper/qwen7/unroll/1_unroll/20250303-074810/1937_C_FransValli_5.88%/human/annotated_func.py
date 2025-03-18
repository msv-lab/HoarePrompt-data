#State of the program right berfore the function call: None of the input variables are explicitly defined in the function signature. However, the problem description implies that the function interacts with an external entity to perform queries and obtain responses. The input variables are n (an integer representing the size of the permutation), and the permutation itself (though it is not directly passed as an argument to the function).
def func():
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: Output State: The output state will consist of two integers, `k` and `best`, which are determined through a series of comparisons within the loop. Specifically, `k` is set to the first value that is found to be less than a subsequent value during the first inner loop, and `best` is set to the first value that is found to be less than `k` during the second inner loop. The exact values of `k` and `best` depend on the input permutation and the results of the comparison queries made to the external entity.
#Overall this is what the function does:The function interacts with an external entity to determine a valid pair of integers \( k \) and \( best \) based on a given permutation. It performs a series of comparison queries to find \( k \) as the first element less than a subsequent element, and then finds \( best \) as the first element less than \( k \). If such elements are found, it outputs \( k \) and \( best \); otherwise, it indicates an error.

