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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 1000\); `a` and `b` are equal (let's denote them as `final_a`); `n` is `final_a`; `l` is the integer value of the binary representation of `final_a` starting from the third character; the outputs are `final_a ^ l` and `l`.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `n`. For each test case, it checks if the number of 1s in the binary representation of `n` is odd. If it is, it prints 'second'. Otherwise, it prints 'first' and then enters a loop where it repeatedly updates `n` based on the parity of the number of 1s in its binary representation until `a` equals `b`. In each iteration of the loop, it calculates `l` as the integer value of the binary representation of `n` starting from the third character, and prints the result of `n XOR l` along with `l`. After the loop, the final state of the program includes `n` being equal to `final_a` (the last value of `a` or `b`), `l` as the integer value of the binary representation of `n` starting from the third character, and the output being `final_a XOR l` and `l`.

