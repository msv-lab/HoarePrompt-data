#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and n is an integer for each test case such that 2 <= n <= 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: t remains an integer such that 1 <= t <= 50, and n is an integer for each test case such that 2 <= n <= 10^3. The loop prints pairs of integers (1, 1), (1, 2), and (i, i) for each i from 3 to n for each test case.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the input, where 1 <= t <= 50, representing the number of test cases. For each test case, it reads another integer `n` from the input, where 2 <= n <= 10^3. The function then prints pairs of integers: (1, 1), (1, 2), and (i, i) for each `i` from 3 to `n`. After the function concludes, the input values `t` and `n` for each test case remain as they were, and the output consists of the printed pairs for each test case.

