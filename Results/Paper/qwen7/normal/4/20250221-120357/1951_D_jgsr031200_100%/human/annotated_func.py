#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
def func_1(n, k):
    if (n == k) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(1)
        #This is printed: 1
        return
        #The program returns k, which is equal to n
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}, and n is greater than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: Output State: `h` is the sum of all integers from 1 to \(n - k + 1\), `n` is 0, `i` is the last element of `costs` which is 1, and `costs` is a list containing two elements, the first element is 0 and the second element is 1.
    #
    #To understand this, let's break it down:
    #- The loop iterates over each element in `costs`. Initially, `costs` contains `[n - k + 1, 1]`.
    #- In the first iteration, `i` is \(n - k + 1\). We compute `curr` as \(n // (n - k + 1)\) and update `h` and `n` accordingly.
    #- In the second iteration, `i` is 1. We compute `curr` as \(n // 1 = n\) and update `h` and `n` again.
    #- In the third iteration, `i` is 1 again, but since `n` has been reduced to 0, `curr` will be 0, and no further changes to `h` or `n` occur.
    #- This process continues until `n` becomes 0, at which point the loop terminates.
    #- The value of `h` accumulates the sum of all integers from 1 to \(n - k + 1\) because `curr` in each iteration is effectively the integer division of `n` by the current `i` in `costs`.
    #- Since `n` is completely consumed, its final value is 0.
    #- The variable `i` takes on the value of the last element in `costs`, which is 1.
    #- The list `costs` is updated to reflect the fact that the first element (which was \(n - k + 1\)) has been fully processed, so it is set to 0, and the second element remains 1.
    if (h < k) :
        print('NO')
        #This is printed: 'NO'
    else :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(*costs)
        #This is printed: 0 1
    #State: `h` is the sum of all integers from 1 to \(n - k + 1\), `n` is 0, `i` is 1, and `costs` is a list containing [0, 1]
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, both of which are positive integers with a constraint of 1 ≤ n, k ≤ 10^18. If `n` equals `k`, the function prints "YES" followed by 1 and 1, then returns `k`. If `n` is less than `k`, it prints "NO" and returns `None`. Otherwise, it calculates the sum of integers from 1 to `n - k + 1` and updates `n` accordingly. If the calculated sum (`h`) is less than `k`, it prints "NO"; otherwise, it prints "YES", 2, the updated `costs` list (which is [0, 1]), and returns `None`.

