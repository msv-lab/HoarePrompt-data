#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
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
        
    #State: The value of `T` is unchanged, and the loop prints the value of `suma - 1` for each iteration of `t` in the range from 0 to `T-1`. The values of `n` and `m` remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` reads an integer `T` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input, where `1 <= a, b <= 2 * 10^6`. The function then calculates a value `suma` based on these inputs and prints `suma - 1` for each test case. The function does not return any value. The values of `n` and `m` are not modified by the function, as they are not used within the function.

