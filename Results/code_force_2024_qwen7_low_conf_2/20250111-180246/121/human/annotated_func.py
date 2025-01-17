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
        
    #State of the program after the  for loop has been executed: `a` and `b` are equal, `n` is the last value assigned to `b` if the count of '1's in the binary representation of `a` is odd, else `n` is the last value assigned to `a`, `l` is the integer value of the binary representation of `n` starting from the third character.
#Overall this is what the function does:Functionality: The function processes multiple test cases, where each test case consists of an integer `t` (1 ≤ t ≤ 1000) followed by an integer `n` (1 ≤ n ≤ 10^18). For each test case, the function checks if the number of '1's in the binary representation of `n` is odd. If it is odd, it prints "second"; otherwise, it prints "first". In the latter case, it further processes `n` by converting its binary representation (starting from the fourth character) to an integer `l` and then prints two values: `n ^ l` and `l`. After this, the function enters a loop where it repeatedly takes two integers `a` and `b` until they are equal. During each iteration, it updates `n` to either `a` or `b` based on whether the number of '1's in the binary representation of `a` is odd. It also converts `n`'s binary representation (starting from the fourth character) to an integer `l` and prints `n ^ l` and `l`. The process continues until `a` equals `b`.

The final state of the program after the function concludes is as follows:
- `a` and `b` are equal, with `b` being the last value assigned to `n` if the count of '1's in the binary representation of `a` is odd, else `n` remains the last value assigned to `a`.
- `l` is the integer value of the binary representation of `n` starting from the third character.
- No other variables retain their values from previous iterations or test cases.

