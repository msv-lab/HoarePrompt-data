#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^6. The sum of all n values across test cases does not exceed 2 · 10^6, and the sum of all m values across test cases does not exceed 2 · 10^6.
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
        
    #State: T lines, each line containing the result of `suma - 1` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `a` and `b`. For each test case, it calculates and prints a result based on a specific formula involving `a` and `b`. The result is the sum of a series of values derived from `a` and `b`, adjusted by subtracting one.

