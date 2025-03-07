#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where each integer is between 1 and 10^9 inclusive; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = []
        
        c = 0
        
        for x in l:
            c += x
            p.append(c)
        
        for _ in range(m):
            a, b = map(int, input().split())
            s = p[b - 1]
            if a - 2 >= 0:
                s -= p[a - 2]
            if b - a + 1 > 1 and s >= 2 * (b - a + 1):
                print('YES')
            else:
                print('NO')
        
    #State: Output State: After the loop executes all iterations, `m` will reflect the total number of queries processed, `a` and `b` will hold the parameters of the last query, `s` will be equal to the element at index `b - 1` of the list `p` minus `m * p[a - 2]` if `a - 2 >= 0`, otherwise it will just be `p[b - 1]`. The list `p` will contain the cumulative sums of the elements in the list `l` up to each index, and `c` will remain as the sum of all elements in the original list `l`. The variable `n` will remain unchanged as it is determined by the input and not modified within the loop.
    #
    #In simpler terms, after running through all the iterations, `m` will show how many times the inner loop ran (i.e., how many queries there were), `a` and `b` will be the values from the last query, `s` will be calculated based on the cumulative sums stored in `p` and the number of queries, `p` will store the cumulative sums of the input list `l`, and `c` will still be the total sum of all elements in `l`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of positive integers and a set of queries. For each query, it calculates the sum of a specified sublist of the list and checks if this sum is at least twice the length of the sublist. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each query.

