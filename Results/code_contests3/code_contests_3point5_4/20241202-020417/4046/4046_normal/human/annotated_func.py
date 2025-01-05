#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer, `l` is the length of the string representation of `n` increased by 1, `ans` is 4444477777, and the length of `l` is even.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `n` is a positive integer, `l` is greater than or equal to 10 and has an even length, `ans` is the minimum value between 4444477777 and the smallest integer value formed by joining the elements of list `x` where count of '7' is equal to count of '4' and is greater than or equal to `n`, `i` is the next even number after the current value, `tem` is the final integer value formed by joining the elements of list `x`, count of '7' is equal to count of '4' in list `x`, and `tem` is the integer value obtained by joining the elements of list `x` where count of '7' is equal to count of '4' and is greater than or equal to `n`, `x` is a list of elements where the count of '7' is equal to the count of '4'.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from user input, calculates the length of the string representation of `n`, adjusts the length to be even if it's odd, then iterates through a range of even numbers starting from the adjusted length. Within the iteration, it generates combinations of '7' and '4' with the same counts, forms integers from these combinations, and finds the smallest integer greater than or equal to `n` that meets the '7' and '4' count condition. Finally, it prints the minimum found integer `ans`. The function does not accept any parameters and does not explicitly return any value.

