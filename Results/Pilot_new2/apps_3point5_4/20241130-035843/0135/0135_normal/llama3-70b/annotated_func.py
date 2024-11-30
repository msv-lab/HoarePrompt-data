#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18.**
def func():
    n, k = map(int, input().split())
    seen = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen:
            print('No')
            exit()
        
        seen.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers such that 1 ≤ n, k ≤ 10^18, `n` and `k` are assigned values obtained from splitting the input string into integers, `seen` is a set containing the remainders of dividing `n` by numbers from 1 to `k`, `i` is `k`, `remainder` is the remainder of dividing `n` by `k`. If any `remainder` is in `seen`, then 'No' has been printed at that point.
    print('Yes')
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from the input. It then iterates from 1 to `k`, calculating the remainder of `n` divided by each number. If any remainder is found in the set `seen`, it prints 'No' and exits. If no repeated remainder is found, it prints 'Yes'. The function does not explicitly return a value.

