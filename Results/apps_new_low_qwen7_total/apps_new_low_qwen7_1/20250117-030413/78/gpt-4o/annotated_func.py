#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 10^5), representing the length of the sequence. The second line contains n integers a_1, a_2, ..., a_n (-10^4 ≤ a_i ≤ 10^4), where the sequence contains at least one subsequence with an odd sum.
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
            
        #State of the program after the  for loop has been executed: `n` is an integer, `a` is a list of `n` integers, `total_sum` is the sum of all integers in the list `a`, `min_positive_odd` is the smallest positive odd integer in the list `a` (or infinity if there are no positive odd integers), `max_negative_odd` is the largest negative odd integer in the list `a` (or negative infinity if there are no negative odd integers).
        result1 = total_sum - min_positive_odd if min_positive_odd != float('inf'
    ) else float('-inf')

result2 = total_sum - max_negative_odd if max_negative_odd != float('-inf'
    ) else float('-inf')

print(max(result1, result2))
    #State of the program after the if-else block has been executed: `n` is an integer, `a` is a list of `n` integers, `total_sum` is the sum of all integers in the list `a`, `min_positive_odd` is the smallest positive odd integer in the list `a` (or infinity if there are no positive odd integers), `max_negative_odd` is the largest negative odd integer in the list `a` (or negative infinity if there are no negative odd integers). If `total_sum` is not divisible by 2, the function continues without further changes. Otherwise, the function calculates `result1` as `total_sum - min_positive_odd` if `min_positive_odd` is not infinity, and `result2` as `total_sum - max_negative_odd` if `max_negative_odd` is not negative infinity, then prints the maximum of `result1` and `result2`.
#Overall this is what the function does:The function reads a sequence of integers from standard input, ensuring that the sequence contains at least one subsequence with an odd sum. It then calculates and prints the maximum value among either subtracting the smallest positive odd number from the total sum, or subtracting the largest negative odd number from the total sum. If there are no positive odd numbers or no negative odd numbers, it handles these cases appropriately by setting the respective variables to infinity or negative infinity, respectively. The function guarantees that it will always produce a result based on the given input constraints.

