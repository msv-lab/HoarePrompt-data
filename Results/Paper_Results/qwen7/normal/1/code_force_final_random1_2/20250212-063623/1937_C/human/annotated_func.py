#State of the program right berfore the function call: None of the input variables are explicitly defined in the function signature. However, the problem implies that the function will interact with an external entity to perform queries and receive responses. The input variables are the number of test cases \( t \) and for each test case, the size of the permutation \( n \) and the results of the queries.
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
        
    #State: Output State: After the loop executes all the iterations, the value of `i` is `n`, `n` is greater than or equal to 2, and `best` is `n-1` if `<` was the result of the query for each pair `(k, i)` where `i` ranges from 1 to `n-1`. If any query resulted in `>`, then `best` remains 0. The variable `k` holds the last value it was updated to during the first phase of the loop, which is `n-1` if all queries in the second phase resulted in `<`. If any query in the second phase resulted in `>`, `k` retains its previous value.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it determines two values: `k` and `best`. It does this by interacting with an external entity through queries. In the first phase, it finds a value `k` such that for all `i` (where `2 ≤ i < n`), the query result is `<`. In the second phase, it finds a value `best` such that for all `i` (where `1 ≤ i < n`), the query result is `<` when comparing `k` with `best` and `i`. Finally, it outputs the values of `k` and `best` for each test case.

