#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18.
def func():
    n, k = map(int, input().split())
    seen = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen:
            print('No')
            exit()
        
        seen.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 1 and 10^18, `k` is an input integer between 1 and 10^18, `seen` is a set that includes the remainders of `n % i` for all `i` from 1 to `k`, where `i` is `k`, and `remainder` is `n % k`.
    print('Yes')
#Overall this is what the function does:The function reads two integers `n` and `k` from input, where both are between 1 and 10^18. It calculates the remainder of `n` divided by every integer from 1 to `k`. If any remainder is repeated during this process, the function prints 'No' and exits. If all remainders are unique, it prints 'Yes'. There are no parameters passed to the function, and it relies on user input for `n` and `k`.

