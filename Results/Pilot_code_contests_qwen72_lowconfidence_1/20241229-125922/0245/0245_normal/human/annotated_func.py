#State of the program right berfore the function call: The input is a string s of length 6, where each character is a digit from '0' to '9'.
def func():
    s, ans = stdin.readline().strip(), float('inf')
    for i in range(0, 10 ** 6):
        cur, tem = i, 0
        
        for j in range(5, -1, -1):
            tem += cur % 10 != int(s[j])
            cur //= 10
        
        if sum([int(x) for x in str(i)[:3]]) == sum([int(y) for y in str(i)[3:]]):
            ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: `s` is a string of length 6, where each character is a digit from '0' to '9'. `ans` is the minimum value of `tem` encountered during the loop execution, where `tem` is the count of positions from 0 to 5 where the digit in `s` is different from the corresponding digit in the current value of `i` (considering `i` as a 6-digit number with leading zeros if necessary). This minimum value is only updated when the sum of the first three digits of `i` is equal to the sum of the last three digits of `i`. If no such `i` is found, `ans` remains `float('inf')`.
    print(ans)
#Overall this is what the function does:The function implicitly accepts a string `s` of length 6, where each character is a digit from '0' to '9'. It searches for the smallest non-negative integer `i` (treated as a 6-digit number with leading zeros if necessary) such that the sum of the first three digits of `i` equals the sum of the last three digits of `i`, and the number of positions from 0 to 5 where the digit in `s` differs from the corresponding digit in `i` is minimized. The function prints this minimum number of differing positions. If no such `i` is found, it prints `float('inf')`.

