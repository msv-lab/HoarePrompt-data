#State of the program right berfore the function call: n is a positive integer representing the initial number of players in the game, and p is a list of positive integers representing the sequence a where 1 ≤ a_1 < a_2 < ... < a_k ≤ 100.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: Output State: `n` will be reduced to 0, assuming the loop continues to execute as long as `n` is greater than or equal to the minimum value in `p`.
    #
    #Explanation: The loop will keep running as long as `n` is greater than or equal to the smallest element in the list `p`. In each iteration, `n` is decreased by the count of elements in `p` that are less than or equal to its current value. This process continues until `n` becomes less than the minimum value in `p`, at which point the condition `n >= min(p)` fails, and the loop terminates. Therefore, the final state of `n` will be 0, provided that the loop can continue reducing `n` to 0 without `n` becoming negative.
    return n
    #The program returns 0
#Overall this is what the function does:The function accepts a positive integer `n` representing an initial value and a list of positive integers `p`. It repeatedly decreases `n` by the count of elements in `p` that are less than or equal to the current value of `n`, as long as `n` is greater than or equal to the smallest element in `p`. After the loop terminates, the function returns 0.

#State of the program right berfore the function call: k and q are positive integers such that 1 <= k, q <= 100. p is a list of k positive integers representing the sequence a where 1 <= a_1 < a_2 < ... < a_k <= 100. qs is a list of q positive integers representing n_i where 1 <= n_i <= 100.
def func_2():
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: Output State: After the loop executes all its iterations, `qs` will be an empty list, `n` will be the last element that was processed, which is the last element in the original `qs` list, `res` will be a list containing the results of applying `func_1(n, p)` to each `n` in `qs` in the order they appeared, `k` will be the value it was initialized to at the start of the loop, and `p` will be the list of integers obtained from the input split and mapped to integers.
    #
    #In simpler terms, after the loop completes all its iterations, `qs` will be empty because all its elements have been processed. The variable `n` will hold the last element of the original `qs` list. The `res` list will contain the results of applying `func_1(n, p)` to each `n` in `qs`, meaning it will have one entry for each element in `qs`. The variables `k` and `p` will retain their initial values from the first iteration of the loop, as they are not modified within the loop body.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two positive integers \( k \) and \( q \), followed by a list \( p \) of \( k \) positive integers and a list \( qs \) of \( q \) positive integers. It then applies another function `func_1` to each element in \( qs \) to check if it exists in \( p \). The result of each check is stored in a list `res`. After processing all elements in \( qs \), it prints the contents of `res` for each test case. Finally, the function returns nothing, as it only prints the results and does not return any value.

