#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut += 1
        
        print(cut + 1)
        
    #State: Output State: `a` is an input string where the total count of occurrences where '1' is immediately followed by '0' is stored in `cut`, `i` is equal to `len(a) - 2`, and `t` is the initial input integer between 1 and 500 inclusive.
    #
    #Explanation: After the loop executes all its iterations, the variable `cut` will hold the total count of occurrences where a '1' is immediately followed by a '0' in the string `a`. The loop runs from `i = 0` to `i = len(a) - 2`, so the final value of `i` will be `len(a) - 2`. The value of `t` remains unchanged as it was the initial input integer specifying how many times the outer loop should run, but since we are considering the inner loop's behavior, it does not affect the final state of `a` and `cut`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a binary string `s`. For each test case, it counts the number of times '1' is immediately followed by '0' in the string `s`. It then prints the count plus one for each test case. The function does not return any value but outputs the results directly.

