#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is an input integer, `l` is the length of the string representation of `n` plus 1, `ans` is 4444477777. If the length of `n` is odd, then the function executes. Otherwise, it does not.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` has a string representation length plus 1 which is odd, `l` is adjusted to meet the loop range condition, `i` is at least `l+1`, `ans` is updated to the minimum value between 4444477777 and `tem`, `tem` holds the integer value of `x` with an even length and an equal count of '4's and '7's, `tem` is greater than or equal to `n`, `x` has an even length and an equal count of '4's and '7's, the length of the string representation of `x` is even, `l` is adjusted to meet the loop range condition for the next iteration, `i` is at least `l+1`, `x` has an equal count of '7's and '4's, `tem` is updated after joining the characters of `x`, `tem` is greater than or equal to `n`, `ans` is the minimum value between `ans` and `tem`
    print(ans)
#Overall this is what the function does:The function takes an integer input `n`, calculates various combinations of '4's and '7's of even length, finds the smallest number among these combinations that is greater than or equal to `n`, and prints this number as output. The function does not accept any parameters and does not return any value.

