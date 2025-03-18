#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9, with the additional information that after the loop executes all iterations, there will be t pairs (a, b) stored in memory.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: 'bob  '
    else :
        print('alice')
        #This is printed: alice
    #State: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9. After the loop executes all iterations, there will be t pairs (a, b) stored in memory. If the sum of a and b is even, the sum is handled accordingly in the if part. If the sum of a and b is not even, the sum is handled accordingly in the else part.
#Overall this is what the function does:The function processes multiple test cases, each containing two positive integers \(a\) and \(b\). For each test case, it checks if the sum of \(a\) and \(b\) is even. If the sum is even, it prints 'bob'. If the sum is odd, it prints 'alice'. After processing all test cases, it returns nothing explicitly but prints 'bob' or 'alice' for each test case based on the condition.

