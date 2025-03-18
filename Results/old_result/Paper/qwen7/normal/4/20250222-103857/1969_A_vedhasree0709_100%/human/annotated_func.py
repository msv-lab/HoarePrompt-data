#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: Output State: The loop will execute for each test case provided by the input. After all iterations of the loop have finished, the value of `i` will be `n`, `n` will be the last input integer processed, `l` will be the last list of integers obtained from the input, `j` will be 0 if the condition `q == i + 1` was never met throughout all iterations, and `p` and `q` will hold the values they had during the last iteration of the while loop. If the condition `q == i + 1` was met at any point during the iterations, the loop would have printed 2 and set `j` to 1, breaking out of the loop early. Since we are considering the final state after all iterations, `j` remains 0, indicating that the condition was never met for any `i` from 0 to `n-1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list \( p \) of \( n \) integers. For each test case, it checks if there exists an index \( i \) (where \( 0 \leq i < n \)) such that the element at index \( p[i] - 1 \) in the list equals \( i + 1 \). If such an index is found, the function prints 2 and breaks out of the loop. If no such index exists after checking all possible \( i \), the function prints 3. The function does not return any value but outputs the result for each test case.

