#State of the program right berfore the function call: The function `func` is incomplete and does not match the problem description. The correct function definition should be `def func(n, m):` where `n` and `m` are positive integers such that 1 ≤ n, m ≤ 2 × 10^6.
def func():
    T = int(input())
    for t in range(T):
        info = input().split()
        
        a, b = int(info[0]), int(info[1])
        
        """for i in range(1,a+1):
                for j in range(4,b+1):
                    if int((j+i)%(j*math.gcd(i,j))) == 0:
                        print(i,j)"""
        
        suma = 0
        
        for i in range(1, b + 1):
            x = (a - i * (i - 1)) // i ** 2 + 1
            if a - i * (i - 1) > 0:
                suma += x
        
        print(suma - 1)
        
    #State: The loop iterates `T` times, reading pairs of integers `(a, b)` from the input. For each pair, it calculates the sum of the number of valid `i` values that satisfy the condition `(a - i * (i - 1)) // i
#Overall this is what the function does:The function reads an integer `T` from the input, which represents the number of test cases. For each test case, it reads a pair of integers `(a, b)` from the input. It then calculates a value based on these integers and prints the result, which is the sum of the number of valid `i` values that satisfy the condition `(a - i * (i - 1)) // i

