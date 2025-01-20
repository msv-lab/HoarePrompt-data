#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100 000, and a is a list of n integers where each integer is either 0 or 1.
def func():
    n = int(input())

a = list(map(int, input().split()))
    if (0 in a and a[:a.index(0)].count(1) > 0) :
        print('YES')

result = []

first_one_index = a.index(1)

first_zero_index = a[first_one_index:].index(0) + first_one_index
        for i in range(first_one_index):
            result.append(str(a[i]) + '->')
            
        #State of the program after the  for loop has been executed: i = first_one_index, result = [str(a[0]) + '->', str(a[1]) + '->', ..., str(a[first_one_index-1]) + '->']
        result.append('(')
        for i in range(first_one_index, first_zero_index):
            result.append(str(a[i]) + '->')
            
        #State of the program after the  for loop has been executed: Output State: `i` is `first_zero_index`, `first_one_index` remains the same, `first_zero_index` remains the same, `result` is a list containing the strings `str(a[first_one_index]) + '->'`, `str(a[first_one_index + 1]) + '->'`, ..., `str(a[first_zero_index - 1]) + '->'`, and `str('(')`.
        #
        #Explanation:
        #1. **Analyze the Code and Initial State**: The loop iterates from `first_one_index` to `first_zero_index - 1`. Each iteration appends `str(a[i]) + '->'` to `result`.
        #2. **Track Variable Changes**: 
        #   - `i` starts at `first_one_index` and increments by 1 in each iteration until it reaches `first_zero_index - 1`.
        #   - `first_one_index` and `first_zero_index` remain constant as they are not updated within the loop.
        #   - `result` starts with the string `str(a[first_one_index]) + '->'` and continues to append new strings as the loop runs.
        #3. **Summarize the Loop Behavior**: The loop will execute `first_zero_index - first_one_index - 1` times. After all iterations, `i` will be equal to `first_zero_index`, and `result` will contain all the required strings.
        #4. **Verify Relationships**: The final state of `result` correctly reflects the appending of strings starting from `str(a[first_one_index]) + '->'` up to `str(a[first_zero_index - 1]) + '->'`, followed by `str('(')`. The variables `first_one_index` and `first_zero_index` remain unchanged, ensuring the relationships are consistent.
        result.append(str(a[first_zero_index]))

result.append(')')
        for i in range(first_zero_index + 1, n):
            result.append('->' + str(a[i]))
            
        #State of the program after the  for loop has been executed: i is `n`, `first_one_index` remains the same, `first_zero_index` remains the same, `result` is a list containing the strings `str(a[first_one_index]) + '->'`, `str(a[first_one_index + 1]) + '->'`, ..., `str(a[first_zero_index - 1]) + '->'`, `str('(') + str(a[first_zero_index]) + ')'`, and for each `i` in the range `first_zero_index + 1` to `n-1`, `'->' + str(a[i])`.
        print(''.join(result))
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an integer, `a` is a list of `n` integers where each integer is either 0 or 1. If `0` is in the list `a` and there is at least one `1` before the first `0`, then `first_one_index` remains the same, `first_zero_index` remains the same, and `result` is a list containing specific strings as described in the if part. Otherwise, the conditions are as described in the else part: 0 is not in the list `a`, or the first occurrence of 0 in `a` does not have any 1s before it.
#Overall this is what the function does:The function processes a list `a` of `n` integers (where each integer is either 0 or 1 and 1 ≤ n ≤ 100,000). It checks if there is at least one 1 before the first 0 in the list. If such a condition is met, it constructs a string with specific formatting and prints 'YES'. Otherwise, it prints 'NO'. Specifically, the function performs the following steps:
1. Reads an integer `n` and a list `a` of `n` integers.
2. Checks if there is at least one 1 before the first 0 in the list.
3. If the condition is met, it constructs a string `result` with the format: `str(a[first_one_index]) + '->'`, `str(a[first_one_index + 1]) + '->'`, ..., `str(a[first_zero_index - 1]) + '->'`, `str('(') + str(a[first_zero_index]) + ')`, and `->str(a[i])` for each `i` in the range `first_zero_index + 1` to `n-1`.
4. Prints the constructed string.
5. If the condition is not met, it simply prints 'NO'.

Potential edge cases include:
- The list `a` consists entirely of 1s.
- The list `a` consists entirely of 0s.
- The list `a` contains no 1s.
- The list `a` contains only one element which is 0.
- The list `a` starts with 0 and does not contain any 1s after it.

