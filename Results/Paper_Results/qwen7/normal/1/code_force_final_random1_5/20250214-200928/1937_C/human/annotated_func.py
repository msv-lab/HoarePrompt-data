#State of the program right berfore the function call: None of the input variables are explicitly defined in the function signature. However, the problem requires the function to handle multiple test cases, where each test case involves finding a pair of indices i and j such that \( p_i \oplus p_j \) is maximized using at most 3n queries. The function must interact with an external entity to ask queries and receive responses. The variable n is an integer representing the size of the permutation, and t is an integer representing the number of test cases.
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
        
    #State: Output State: `best` is 5, `n` must be greater than 1, `i` is `n`, `k` is 5, and `res` is an input string.
    #
    #Explanation: The loop runs from `i=2` to `i=n-1`. Given that the loop has executed all its iterations, it means `i` has reached `n-1` and the loop has completed. Therefore, `i` is now equal to `n`. The value of `best` remains 5 because it was updated to the last value of `i` (which is 5) during the loop's execution. The value of `k` remains 5 as it is only updated inside the loop when `res` is '<', and since `res` was always '<' in the previous iterations, `k` was updated to the current value of `i` (which is 5) in the last iteration. The value of `n` must be greater than 1 as it is the size of the permutation, and `res` remains an input string as it is read from the input in each iteration.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it finds a pair of indices \(i\) and \(j\) such that \(p_i \oplus p_j\) is maximized using at most 3n queries. It interacts with an external entity to ask queries and receives responses. After completing the queries for each test case, it outputs the indices \(k\) and \(best\) that maximize \(p_i \oplus p_j\).

