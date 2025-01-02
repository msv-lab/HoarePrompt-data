#State of the program right berfore the function call: a is a list of non-negative integers representing the amount of garbage produced each day, and k is a positive integer representing the capacity of each garbage bag such that 1 ≤ k ≤ 10^9.
def func_1(a, k):
    bags, carry = 0, 0
    for i in a:
        if carry != 0:
            bags += 1
            i = max(0, i - carry)
        
        bags += i // k
        
        carry = i % k
        
    #State of the program after the  for loop has been executed: To determine the final output state of the loop, we need to consider the behavior of the loop over all iterations. Let's break down the logic step by step:
    #
    #1. **Initial State:**
    #   - `a` is a list of non-negative integers.
    #   - `k` is a positive integer such that \(1 \leq k \leq 10^9\).
    #   - `bags` is initialized to 0.
    #   - `carry` is initialized to 0.
    #
    #2. **Loop Behavior:**
    #   - For each element `i` in the list `a`:
    #     - If `carry` is not 0, increment `bags` by 1 and update `i` to `max(0, i - carry)`.
    #     - Increment `bags` by `i // k`.
    #     - Update `carry` to `i % k`.
    #
    #3. **Final State After All Iterations:**
    #   - The loop will iterate through all elements of `a`.
    #   - For each element `i` in `a`, the number of bags used is calculated based on the current value of `carry` and the value of `i`.
    #   - The final value of `bags` will be the total number of bags used to carry all the garbage.
    #   - The final value of `carry` will be the remaining garbage that could not fit into the last full bag.
    #
    #4. **Detailed Final State:**
    #   - `a` remains a list of non-negative integers (unchanged).
    #   - `k` remains a positive integer such that \(1 \leq k \leq 10^9\) (unchanged).
    #   - `bags` will be the total number of bags used to carry all the garbage.
    #   - `carry` will be the remaining garbage that could not fit into the last full bag.
    #
    #If the list `a` is empty, the loop does not execute, and the values of `bags` and `carry` remain 0.
    #
    #Therefore, the output state after all iterations of the loop have finished is:
    #**`a` is a list of non-negative integers, `k` is a positive integer such that \(1 \leq k \leq 10^9\), `bags` is the total number of bags used to carry all the garbage, `carry` is the remaining garbage that could not fit into the last full bag.**
    if (carry != 0) :
        bags += 1
    #State of the program after the if block has been executed: *`a` is a list of non-negative integers, `k` is a positive integer such that \(1 \leq k \leq 10^9\), `bags` is the total number of bags used to carry all the garbage. If `carry` is not 0, `bags` is incremented by 1, and `carry` remains the remaining garbage that could not fit into the last full bag. Otherwise, `bags` and `carry` retain their final values from the loop.
    return bags
    #The program returns the total number of bags used to carry all the garbage. If `carry` is not 0, `bags` is incremented by 1, and `carry` remains the remaining garbage that could not fit into the last full bag. Otherwise, `bags` and `carry` retain their final values from the loop.
#Overall this is what the function does:The function `func_1` takes two parameters: a list `a` of non-negative integers representing the amount of garbage produced each day, and a positive integer `k` representing the capacity of each garbage bag (1 ≤ k ≤ 10^9). The function calculates and returns the total number of garbage bags needed to carry all the garbage. 

-

#State of the program right berfore the function call: k is an integer such that 1 ≤ k ≤ 10^9, and a is a list of non-negative integers where each element a_i satisfies 0 ≤ a_i ≤ 10^9.
def func_2():
    _, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    print(min(func_1(a, k), func_1(a[::-1], k)))
#Overall this is what the function does:The function `func_2` reads two inputs: an integer `k` (1 ≤ k ≤ 10^9) and a list of non-negative integers `a` (where each element `a_i` satisfies 0 ≤ a_i ≤ 10^9). It then computes the minimum value between the result of `func_1(a, k)` and `func_1(a[::-1], k)`, where `a[::-1]` is the reversed list of `a`. Finally, it prints this minimum value. The function does not return any value; instead, it directly outputs the result to the console. The state of the program after the function concludes is that the input values `k` and `a` remain unchanged, and the computed minimum value has been printed.

