#State of the program right berfore the function call: The input consists of two lines. The first line contains an integer n (1 ≤ n ≤ 10^5), representing the length of the sequence. The second line contains n integers a_1, a_2, ..., a_{n} (-10^4 ≤ a_{i} ≤ 10^4), representing the sequence. The sequence contains at least one subsequence with an odd sum.
def func():
    n = int(input())

a = list(map(int, input().split()))

total_sum = sum(a)

min_positive_odd = float('inf')

max_negative_odd = float('-inf')
    if (total_sum % 2 != 0) :
        print(total_sum)
    else :
        for num in a:
            if num % 2 != 0:
                if num > 0:
                    min_positive_odd = min(min_positive_odd, num)
                else:
                    max_negative_odd = max(max_negative_odd, num)
            
        #State of the program after the  for loop has been executed: `n` is an input integer, `a` is a list of `n` integers, `total_sum` is the sum of the elements in `a`, `min_positive_odd` is the minimum positive odd number encountered in the list `a` (or positive infinity if no positive odd numbers are present), `max_negative_odd` is the maximum negative odd number encountered in the list `a` (or negative infinity if no negative odd numbers are present).
        result1 = total_sum - min_positive_odd if min_positive_odd != float('inf'
    ) else float('-inf')

result2 = total_sum - max_negative_odd if max_negative_odd != float('-inf'
    ) else float('-inf')

print(max(result1, result2))
    #State of the program after the if-else block has been executed: `n` is the input integer, `a` is a list of `n` integers, `total_sum` is the sum of the elements in `a`, `min_positive_odd` is the minimum positive odd number encountered in the list `a` (or positive infinity if no positive odd numbers are present), `max_negative_odd` is the maximum negative odd number encountered in the list `a` (or negative infinity if no negative odd numbers are present). If `total_sum` is odd, `min_positive_odd` remains as positive infinity and `max_negative_odd` remains as negative infinity. Otherwise, `min_positive_odd` and `max_negative_odd` reflect the minimum positive odd and maximum negative odd numbers in the list `a`, respectively.
#Overall this is what the function does:The function reads an integer \( n \) and a sequence of \( n \) integers from standard input. It calculates the total sum of the sequence and finds the minimum positive odd number and the maximum negative odd number within the sequence. Based on the parity of the total sum, it either prints the total sum directly or computes two potential new sums: one by subtracting the minimum positive odd number from the total sum (if it exists), and another by subtracting the maximum negative odd number from the total sum (if it exists). Finally, it prints the larger of these two computed sums. The function does not return a value but modifies the output stream directly. Potential edge cases include sequences without positive or negative odd numbers, which are handled by setting `min_positive_odd` to positive infinity and `max_negative_odd` to negative infinity, ensuring that the resulting sums are appropriately set to negative infinity.

