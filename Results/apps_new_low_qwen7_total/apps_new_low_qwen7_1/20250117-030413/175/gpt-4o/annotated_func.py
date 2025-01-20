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
            
        #State of the program after the  for loop has been executed: n is 5, a is [0, 1, 0, 1, 1], first_one_index is 1, first_zero_index is 1, result is ['0->'].
        result.append('(')
        for i in range(first_one_index, first_zero_index):
            result.append(str(a[i]) + '->')
            
        #State of the program after the  for loop has been executed: Let's analyze the given loop and the provided states step by step.
        #
        #### Analyze the Code and Initial State
        #The loop iterates over the indices defined by `first_one_index` and `first_zero_index`. The loop body appends strings to the `result` list based on the values of `a[i]`.
        #
        #### Track Variable Changes
        #- **Invariants**: 
        #  - `n` remains unchanged as it is not modified in the loop.
        #  - `a` remains unchanged as it is not modified in the loop.
        #  - `first_one_index` and `first_zero_index` are used to define the range but are not modified within the loop itself.
        #- **Variables Modified in the Loop**:
        #  - `result`: Strings are appended to this list.
        #  - `i`: This variable is incremented within the loop and is used to iterate through the specified range.
        #
        #### Summarize the Loop Behavior
        #The loop will append strings to `result` starting from `first_one_index` up to `first_zero_index - 1`. The loop continues until `i` reaches `first_zero_index - 1`.
        #
        #### Verify Relationships
        #From the provided states, we can see:
        #- After the loop executes 1 time, `result` becomes `['0->', '(', '0->']`.
        #- After the loop executes 2 times, `result` becomes `['0->', '(', '0->', '1->']`, and `i` is 2.
        #- After the loop executes 3 times, `result` becomes `['0->', '(', '0->', '1->', '1->']`, and `i` is 4.
        #
        #Since `first_zero_index` must be greater than `first_one_index` (which is 1), and the loop appends one element per iteration, we can infer that the loop will continue appending elements until `i` reaches `first_zero_index - 1`.
        #
        #### Determine the Final Output State
        #To find the final state after all iterations, we need to consider the maximum possible value of `first_zero_index` and the maximum number of times the loop can execute.
        #
        #- If `first_zero_index` is 5, the loop would execute 3 times (from index 1 to 3).
        #- The final state of `result` would be: `['0->', '(', '0->', '1->', '1->']`.
        #
        #Since `first_zero_index` is not specified to be more than 5, and given the pattern, we assume `first_zero_index` is 5 (the highest possible value).
        #
        #Thus, the final state of `result` will be `['0->', '(', '0->', '1->', '1->']`.
        #
        #### Conclusion
        #Output State: `n` is 5, `a` is [0, 1, 0, 1, 1], `first_one_index` is 1, `first_zero_index` is 5, `result` is ['0->', '(', '0->', '1->', '1->'].
        result.append(str(a[first_zero_index]))

result.append(')')
        for i in range(first_zero_index + 1, n):
            result.append('->' + str(a[i]))
            
        #State of the program after the  for loop has been executed: n is 5, a is [0, 1, 0, 1, 1], first_one_index is 1, first_zero_index is 5, result is ['1', '0', '1', '(', '1', ')', '->1', '->0', '->1'].
        print(''.join(result))
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is 5, `a` is [0, 1, 0, 1, 1]. If 0 is in the list `a` and the count of 1's in the sublist `a[:a.index(0)]` is greater than 0, then `first_one_index` is 1, `first_zero_index` is 5, `result` is ['1', '0', '1', '(', '1', ')', '->1', '->0', '->1'], and the string '101(1)->1->0->1' is printed. Otherwise, 0 is in the list `a` and the count of 1's in the sublist `a[:a.index(0)]` is not greater than 0.
#Overall this is what the function does:The function `func` accepts a list `a` of integers where each integer is either 0 or 1, and returns a string based on certain conditions. Specifically, it checks if the list `a` contains a 0 and if the sublist before the first 0 contains at least one 1. If both conditions are met, it constructs a specific string and prints it. Otherwise, it prints 'NO'.

