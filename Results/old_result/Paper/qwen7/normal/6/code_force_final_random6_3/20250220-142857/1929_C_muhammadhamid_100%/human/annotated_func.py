#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, k is an integer such that 2 ≤ k ≤ 30, x is an integer such that 1 ≤ x ≤ 100, and a is an integer such that 1 ≤ a ≤ 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: Output State: The loop will execute `x` times, with `i` ranging from 0 to `x-1`. After all iterations, `s` will be \(2^x - 1\), `k` will remain as the input integer, `x` will remain as the input integer, and `i` will be equal to `x-1`.
    #
    #Explanation: After all iterations of the loop, the variable `s` will undergo the operation `s += s // (k - 1) + 1` a total of `x` times, starting from `s = 1`. This results in `s` being transformed into \(2^x - 1\). The variable `i` will increment from 0 up to `x-1` during the loop, and thus will be equal to `x-1` after the loop completes. The values of `k` and `x` remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function processes multiple inputs where each input consists of integers `k`, `x`, and `a`. For each set of inputs, it calculates the value of `s` starting from 1 and updating it `x` times using the formula `s += s // (k - 1) + 1`. After these calculations, it compares `a` with `s` and prints 'Yes' if `a` is greater than or equal to `s`, otherwise it prints 'No'. The function does not return any value but prints the result for each input set.

