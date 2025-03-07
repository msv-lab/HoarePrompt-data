#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. Each test case consists of three integers n, f, and k such that 1 <= f, k <= n <= 100, followed by a list of n integers a_i where 1 <= a_i <= 100.
def func():
    t = int(input())
    for _ in range(t):
        n, f, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        favorite_value = a[f - 1]
        
        sorted_a = sorted(a, reverse=True)
        
        removed_count = 0
        
        for i in range(k):
            if sorted_a[i] == favorite_value:
                removed_count += 1
        
        favorite_count = sorted_a.count(favorite_value)
        
        if removed_count == favorite_count:
            print('YES')
        elif removed_count == 0:
            print('NO')
        else:
            print('MAYBE')
        
    #State: Output State: The output consists of 'YES', 'NO', or 'MAYBE' for each iteration based on the conditions specified in the loop. For each test case (determined by the value of `t`), the program processes the list `a`, finds the `favorite_value` at index `f-1`, sorts the list in descending order, counts how many times `favorite_value` appears in the original list, and checks if the number of times `favorite_value` is removed (when it's the largest) equals its frequency in the original list. If they match, it prints 'YES'. If `favorite_value` never gets removed, it prints 'NO'. Otherwise, it prints 'MAYBE'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( n \), \( f \), and \( k \), followed by a list of \( n \) integers \( a_i \). For each test case, it determines whether a specific value (the \( f \)-th element in the list) will be removed exactly as many times as it appears in the original list when the list is sorted in descending order and the first \( k \) elements are considered. If the count of the specific value matches its frequency in the original list, it outputs 'YES'; if the specific value never gets removed, it outputs 'NO'; otherwise, it outputs 'MAYBE'. The function implicitly accepts the number of test cases \( t \) as input and returns no explicit value but prints the result for each test case.

