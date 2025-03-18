#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func():
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: Output State: The list `p` contains all integers from 1 up to and including `a`.
    #
    #Explanation: After the loop has executed all its iterations, `i` will be equal to `a + 1` because the loop increments `i` by 2 starting from 2 until it exceeds `a`. The list `p` will contain all integers from 1 up to and including `a` because the loop alternates between adding even and odd numbers to the list `p`. Specifically, it starts by adding all even numbers from 2 up to the largest even number less than or equal to `a`, and then it adds all odd numbers from 1 up to `a` if `a` is odd, or up to `a - 1` if `a` is even. Therefore, the final list `p` will include every integer from 1 to `a`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `a` and constructs a list `p` containing all integers from 1 to `a`. It alternates between adding even and odd numbers to the list `p`. After processing all test cases, it prints the list `p` for each test case.

