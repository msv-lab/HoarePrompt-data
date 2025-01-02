#State of the program right berfore the function call: l and r are non-negative integers such that 1 ≤ l ≤ r ≤ 10^18.
def func_1():
    lower, upper = map(int, raw_input().split())
    res = 0
    for val in range(1, 10):
        if lower <= val <= upper:
            res += 1
        
    #State of the program after the  for loop has been executed: `lower` is an input integer, `upper` is an input integer, `res` is the count of integers between `lower` and `upper` inclusive.
    for length in range(2, 19):
        for startend in range(1, 10):
            alreadyval = startend * pow(10, length - 1) + (0 if length == 1 else
                startend)
            smallestpos = max(0, (lower - alreadyval + 9) / 10)
            largestpos = min(pow(10, length - 2) - 1, (upper - alreadyval) / 10)
            res += max(0, largestpos - smallestpos + 1)
        
    #State of the program after the  for loop has been executed: `length` is 19, `startend` is 9, `alreadyval` is \(9 \times 10^{18} + 9\), `smallestpos` is \(max(0, (lower - 9 \times 10^{18}) / 10)\), `largestpos` is \(min(10^{17} - 1, (upper - 9 \times 10^{18} - 9) / 10)\), `res` is the total count of valid integers between `lower` and `upper`.
    print(res)
#Overall this is what the function does:The function accepts two parameters `lower` and `upper`, both non-negative integers such that \(1 \leq lower \leq upper \leq 10^{18}\). It calculates and returns the count of integers within the range `[lower, upper]` that can be represented using exactly 19 digits. This includes numbers from \(10^{18}\) to \(9999999999999999999\) (i.e., 19-digit numbers).

The function performs the following steps:
1. It initializes `res` to 0.
2. It counts the number of single-digit integers (1 through 9) that fall within the range `[lower, upper]`.
3. For each digit length from 2 to 19, it iterates over all possible starting digits (from 1 to 9).
4. For each starting digit and length, it calculates the smallest and largest positions of numbers that fit within the given range.
5. It updates `res` by adding the count of valid numbers for each combination of length and starting digit.

The function handles edge cases such as when `lower` or `upper` is less than \(10^{18}\) or greater than \(9999999999999999999\). If `lower` or `upper` is outside the valid range, the function will still execute but the counts will only consider the valid portion of the range.

