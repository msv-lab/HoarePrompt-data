#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains the array a of size n (1 ≤ n ≤ 2·10^5) with elements a_1, a_2, ..., a_n (1 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `n` is an input integer greater than 0, `l` is a list of integers input by the user, `x` is `n - 1`, `a` is the smallest integer in the list `l`, `b` is the second smallest integer in the list `l` (or `float('inf')` if there is no second smallest integer), and `c` is the count of integers in `l` that are greater than both `a` and `b` for each test case.
#Overall this is what the function does:The function processes a series of test cases, each containing an array of integers. For each test case, it identifies the smallest and second smallest integers in the array. It then counts how many integers in the array are greater than both of these values. The function prints the count for each test case. After processing all test cases, the function concludes, and the final state includes the printed counts for each test case.

