#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: The loop has completed all its iterations, `i` is equal to `int(input())`, `s` is the last input string received, `a` is the integer value of the first element in the list obtained by splitting `s` on spaces, and `b` is the integer value of the second element in the list obtained by splitting `s` on spaces.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: The loop has completed all its iterations, `i` is equal to the integer value of the input, `s` is the last input string received, `a` is the integer value of the first element in the list obtained by splitting `s` on spaces, and `b` is the integer value of the second element in the list obtained by splitting `s` on spaces. If the sum of `a` and `b` is even, the sum is even. If the sum of `a` and `b` is odd, the sum is odd.
#Overall this is what the function does:The function processes a series of test cases, each containing three positive integers: `t`, `a`, and `b`. For each test case, it reads `t` pairs of integers `a` and `b`, calculates their sum, and prints 'bob' if the sum is even, or 'alice' if the sum is odd. After processing all test cases, the function does not return any value but prints 'bob' or 'alice' for each pair of integers `a` and `b` based on the parity of their sum.

