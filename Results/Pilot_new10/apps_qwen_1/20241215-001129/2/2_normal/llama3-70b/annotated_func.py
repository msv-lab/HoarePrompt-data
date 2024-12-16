#State of the program right berfore the function call: The input is a string representing a positive integer x such that 1 ≤ x ≤ 10^18.
def func():
    x = int(input())
    max_sum = 0
    max_num = 0
    for i in range(1, x + 1):
        digit_sum = sum(int(digit) for digit in str(i))
        
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = i
        
    #State of the program after the  for loop has been executed: `x` is the final integer value within the range of 1 to \(10^{18}\); `max_sum` is the maximum digit sum encountered during the loop; `max_num` is the number corresponding to the maximum digit sum.
    print(max_num)
#Overall this is what the function does:The function accepts a string input representing a positive integer \( x \) within the range 1 to \( 10^{18} \) (inclusive) and prints the number with the largest digit sum within the range 1 to \( x \).

