#State of the program right berfore the function call: n and k are integers such that 1 <= n, k <= 10^18.**
def func():
    n, k = map(int, input().split())
    seen = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen:
            print('No')
            exit()
        
        seen.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` is not involved in loop execution, `k` is greater than or equal to 1, `seen` is a set containing all remainders from `n % i` for `i` ranging from 1 to `k`. If any remainder is repeated, the program prints 'No'.
    print('Yes')
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from input. It then iterates from 1 to `k` inclusive, calculating the remainder of `n` divided by each `i`. If any remainder is repeated, it prints 'No' and exits the program. If no remainders are repeated, it prints 'Yes'. The function does not explicitly return any value.

