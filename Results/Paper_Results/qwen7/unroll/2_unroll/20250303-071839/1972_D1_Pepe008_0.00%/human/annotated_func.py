#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
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
        
    #State: Output State: The value of `T` is reduced to 0 after all iterations of the loop have finished. For each iteration `t` from 0 to `T-1`, the loop processes the inputs `a` and `b`, calculates the sum `suma` based on these inputs, and prints `suma - 1`. The final state of `T` is 0 since it starts from 1 and is decremented by 1 in each iteration until it reaches 0.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers \(a\) and \(b\). For each test case, it calculates a sum based on these integers using a specific formula and prints the result minus one. After processing all test cases, the function ensures that the counter \(T\) is reduced to zero.

