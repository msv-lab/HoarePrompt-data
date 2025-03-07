#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func():
    T = int(input())
    for t in range(T):
        info = input().split()
        
        a, b = int(info[0]), int(info[1])
        
        suma = 0
        
        for i in range(1, b + 1):
            x = (a - i * (i - 1)) // i ** 2 + 1
            if (a - i * (i - 1)) // i ** 2 + 1 > 0:
                suma += x
                if (a - i * (i - 1)) % i ** 2 == 0 and i * (i - 1) % i ** 2 == 0:
                    suma += 1
        
        print(suma - 2)
        
    #State: Output State: The output state is a series of integers, each corresponding to the value of `suma - 2` for each input pair `(a, b)` provided by the user within the range specified by `T`. Each integer represents the sum calculated according to the given formula, minus 2, for each iteration of the outer loop.
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers \(a\) and \(b\). For each test case, it calculates a sum based on a specific formula involving \(a\) and \(b\), and prints the result of this sum minus 2. The function reads the number of test cases from the first line of input, followed by pairs of integers for each test case. The final output consists of one integer per test case, representing the calculated sum minus 2.

