#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two positive integers n and m such that 1 ≤ n, m ≤ 2 ⋅ 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 ⋅ 10^6.
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
        
    #State: The sequence of results for each test case, where each result is the value of `suma - 1` computed for the respective `a` and `b` values.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers `a` and `b`. For each test case, it computes a specific sum based on these integers and outputs the result minus one.

