#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9.**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *n is a positive integer such that 1 ≤ n ≤ 10^9; l is the length of the string representation of n. If l is an odd number, then l is now an even number, and ans is 4444477777. Otherwise, there is no change in the values of n, l, and ans.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ n ≤ 10^9, `l` is an even number, `ans` is updated to the minimum value of `tem` that satisfies the conditions, `i` is 10, `x` is a tuple containing only '7' and '4', `tem` is an integer value, the program state remains the same if the conditions for `tem` are not met.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, calculates the length of the string representation of `n`, adjusts the length to be even if it is odd, and then iterates through certain combinations of '7' and '4' digits to find the smallest integer greater than or equal to `n` where the count of '7's is equal to the count of '4's. Finally, it prints the calculated integer `ans`. The function does not accept any parameters and does not return any value.

