#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 10^18.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        if bin(n).count('1') & 1:
            print('second')
        else:
            print('first')
            l = int(bin(n)[3:], 2)
            print(n ^ l, l)
        
        while True:
            a, b = map(int, input().split())
            if a == b:
                break
            n = b if bin(a).count('1') & 1 else a
            l = int(bin(n)[3:], 2)
            print(n ^ l, l)
        
    #State of the program after the  for loop has been executed: Output State:
#Overall this is what the function does:The function processes a series of test cases defined by the integer `t` (where \(1 \leq t \leq 1000\)). For each test case, it reads an integer `n` (where \(1 \leq n \leq 10^{18}\)) and performs the following operations:

1. Determines if the number of set bits in `n` is odd. If it is, the function prints 'second'.
2. If the number of set bits is even, the function prints 'first' and then proceeds to transform `n` based on certain conditions.
   - It calculates a new value `l` derived from the binary representation of `n`.
   - It prints the result of `n XOR l` along with `l`.
3. After these operations, it enters a loop that continues until two consecutive inputs are equal. In each iteration of the loop, it updates `n` based on the parity of the set bits in the current value of `a`. It then repeats the process of calculating `l` and printing `n XOR l` and `l`.

The function does not return any explicit value. Instead, it outputs a sequence of integers and strings during its execution.

