#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: t is an input integer between 1 and 50, inclusive, i is 3, and n is an input integer.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( t \) and \( n \). For each test case, it prints a sequence of pairs of integers. If \( n = 3 \), it prints "2 3". Otherwise, it prints "2 4" followed by pairs of integers from "4" to \( n \) paired with themselves. The function does not return any value but outputs the specified sequences of pairs to the console.

