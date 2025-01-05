#State of the program right berfore the function call: n is a positive integer greater than or equal to 1 and less than or equal to 10^9.**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *`n` is a positive integer between 1 and 10^9, `l` is between 1 and 10, `ans` is 4444477777. If `l` is odd, no change in the variables occurs.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 10^9, `l` is an even number between 1 and 10, `ans` is the minimum value between `ans` and `tem`, where `tem` is an integer value obtained by joining the characters in `x` which is greater than or equal to `n`. If no combination of '7' and '4' characters satisfies the conditions, the initial state is retained.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input and then calculates the minimum integer greater than or equal to `n` which has an equal count of '7' and '4' characters when represented as a string of even length. This is done by iterating through possible combinations of '7' and '4' characters. The calculated minimum integer is then printed as the output. The function does not accept any parameters and operates solely on user input.

