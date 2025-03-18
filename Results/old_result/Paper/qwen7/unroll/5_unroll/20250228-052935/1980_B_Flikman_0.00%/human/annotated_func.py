#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for all i.
def func():
    t = int(input())
    for _ in range(t):
        n, f, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        favorite_value = a[f - 1]
        
        same_value_count = 0
        
        for value in a:
            if value == favorite_value:
                same_value_count += 1
        
        greater_count = 0
        
        for value in a:
            if value > favorite_value:
                greater_count += 1
        
        if greater_count >= k:
            print('YES')
        elif greater_count + same_value_count <= k:
            print('NO')
        else:
            print('MAYBE')
        
    #State: Output State: The output state depends on the input values provided within each iteration of the loop. For each iteration, the variables `n`, `f`, `k`, and `a` are updated based on user input, and the loop prints either 'YES', 'NO', or 'MAYBE' based on the conditions specified. The final state will consist of these printed outputs for each iteration, with no specific numerical values since the exact inputs are not provided.
#Overall this is what the function does:The function processes up to 1000 test cases. For each test case, it reads three integers \( n \), \( f \), and \( k \), and a list of \( n \) integers \( a \). It then determines whether there are at least \( k \) elements in \( a \) that are greater than the element at index \( f-1 \), or if the number of elements equal to the element at index \( f-1 \) plus the number of elements greater than it is less than or equal to \( k \). Based on this determination, it prints either 'YES', 'NO', or 'MAYBE'. After processing all test cases, the function outputs the results for each case.

