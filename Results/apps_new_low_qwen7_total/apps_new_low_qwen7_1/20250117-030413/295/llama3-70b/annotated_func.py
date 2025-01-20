#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 24, and a_1, a_2, ..., a_{n} are integers such that 28 ≤ a_{i} ≤ 31.
def func():
    n = int(input())

a = list(map(int, input().split()))

b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

f = False
    for i in range(12):
        if all(a[j] == b[(i + j) % 12] for j in range(n)):
            f = True
        
        if i == 11 and not f:
            break
        
        if all(a[j] == b[(i + j) % 12 + 12] for j in range(n)):
            f = True
        
        if i == 11 and not f:
            break
        
    #State of the program after the  for loop has been executed: Output State: \(i\) is either 0 or 11, `f` is True, and lists `a` and `b` must satisfy the condition \(a[j] == b[(i + j) \% 12]\) for all \(j\) in the range \(n\). If \(i\) is 11 and \(f\) is False, the loop will break out, but since `f` is set to True in the if conditions, this scenario is not possible. Therefore, `f` will always be True after the loop completes, as long as the condition \(a[j] == b[(i + j) \% 12]\) holds for some \(i\) in the range of 0 to 11.
    if f :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`i` is either 0 or 11, `f` is True, and lists `a` and `b` must satisfy the condition \(a[j] == b[(i + j) \% 12]\) for all \(j\) in the range \(n\). If the condition \(a[j] == b[(i + j) \% 12]\) holds for the current `i`, the output is 'YES' and the state remains unchanged. Otherwise, the output is 'NO' and the state remains unchanged.
#Overall this is what the function does:The function accepts two parameters: `n`, an integer such that \(1 \leq n \leq 24\), and `a`, a list of integers where each element \(a_i\) satisfies \(28 \leq a_i \leq 31\). The function then checks if the elements of the list `a` can be aligned with the list `b` (which contains the number of days in each month of a year) in a cyclic manner such that each element of `a` matches an element of `b`. If such an alignment exists, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result directly.

