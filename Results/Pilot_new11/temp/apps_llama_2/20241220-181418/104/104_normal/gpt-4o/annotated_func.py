#State of the program right berfore the function call: The input is a list of integers where the first integer represents the number of elements in the array (n), and the rest of the integers represent the array elements (a_i) such that 1 <= n <= 100 and 1 <= a_1 < a_2 <... < a_n <= 10^3.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100 (inclusive), `a` is a list of integers where `a[0]` equals the original value of `n` and `a[1:]` holds the array elements `a_i` where 1 <= `a_i` <= 10^3, `max_erase` is the maximum gap between any two consecutive numbers in the sequence starting from `n` and considering elements in `a[1:]`, and `i` is `n-1`.
    print(max_erase)
#Overall this is what the function does:The function calculates and prints the maximum gap between any two consecutive numbers in a given sequence of integers. It accepts input from the user, where the first input is the number of elements (n) and the second input is a list of integers (a_i) representing the sequence. The function assumes the input sequence is valid, with 1 <= n <= 100 and 1 <= a_1 < a_2 <... < a_n <= 10^3. However, it does not perform any error checking on the input, so it does not handle potential edge cases such as invalid or out-of-range input values. After execution, the program state includes the printed maximum gap between any two consecutive numbers in the sequence, but the original input sequence and variables (n, a, max_erase) are not returned or preserved. The function has no explicit return value, as it prints the result directly to the console.

