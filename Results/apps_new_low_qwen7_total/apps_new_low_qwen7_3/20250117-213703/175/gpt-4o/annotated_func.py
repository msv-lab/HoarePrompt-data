#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100 000, and a_1, a_2, ..., a_{n} are a list of n integers where each a_i is either 0 or 1.
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
            
        #State of the program after the  for loop has been executed: n is 5, a is [1, 0, 1, 0, 1], first_one_index is 3, first_zero_index is 0, result is ['0->', '1->', '1->', '0->', '1->', '1->'].
        result.append('(')
        for i in range(first_one_index, first_zero_index):
            result.append(str(a[i]) + '->')
            
        #State of the program after the  for loop has been executed: Let's analyze the given Python loop and track the changes in the variables step by step.
        #
        #### Step 1: Analyze the Code and Initial State
        #
        #The loop iterates over a range defined by `first_one_index` and `first_zero_index`. Specifically, it appends the binary value of elements in array `a` at each index between `first_one_index` and `first_zero_index` (exclusive) to the `result` list.
        #
        #### Step 2: Track Variable Changes
        #
        #- **Invariants:**
        #  - `n` remains unchanged because it is not involved in the loop or any modification within the loop.
        #  - `a` remains unchanged because it is not modified inside the loop.
        #  - `first_one_index` and `first_zero_index` are not updated within the loop; hence, they remain constant.
        #
        #- **Variables affected by the loop:**
        #  - `i`: This variable changes with each iteration and is used to access elements in the array `a`.
        #
        #### Step 3: Summarize the Loop Behavior
        #
        #The loop will execute as long as `first_one_index < first_zero_index`. For each iteration, it appends the binary value of `a[i]` followed by `'->'` to `result`.
        #
        #Given the provided outputs, we can infer the following:
        #- After the loop has executed, `i` takes the value of the last index processed, which is `first_zero_index - 1`.
        #- The loop stops when `i` reaches `first_zero_index - 1`.
        #
        #### Step 4: Verify Relationships
        #
        #From the outputs provided:
        #- After 1 execution: `i` becomes 2 (since `first_zero_index` is 3, `i` goes up to 2).
        #- After 2 executions: `i` becomes 3 (since `first_zero_index` is still 3, `i` goes up to 3).
        #- After 3 executions: `i` becomes 4 (since `first_zero_index` is 3, `i` would go up to 4 but stops).
        #
        #This indicates that the loop will stop when `i` equals `first_zero_index - 1`, which is 2 in the initial state. Therefore, the loop will execute exactly twice.
        #
        #### Final Output State
        #
        #Since the loop executes twice and appends the binary values of the specified indices in `a` to `result`, the final `result` list will contain the appended values for the indices between `first_one_index` and `first_zero_index` (inclusive of the start and exclusive of the end).
        #
        #Given the initial state:
        #- `a` = [1, 0, 1, 0, 1]
        #- `first_one_index` = 3
        #- `first_zero_index` = 0
        #
        #The indices to append are 3 and 4:
        #- `a[3]` is 0
        #- `a[4]` is 1
        #
        #Thus, the final `result` will be:
        #- `result` = ['0->', '1->', '0->', '1->']
        #
        #### Output State: `n` is 5, `a` is [1, 0, 1, 0, 1], `first_one_index` is 3, `first_zero_index` is 0, `i` is 4, `result` is ['0->', '1->', '0->', '1->']
        result.append(str(a[first_zero_index]))

result.append(')')
        for i in range(first_zero_index + 1, n):
            result.append('->' + str(a[i]))
            
        #State of the program after the  for loop has been executed: ### Analysis
        #
        ##### Step 1: Analyze the Code and Initial State
        #The loop iterates over the indices of the list `a` starting from `first_zero_index + 1` up to `n - 1`. Inside the loop, it appends a string to the `result` list by combining `'->'` and the value of `a[i]`.
        #
        ##### Step 2: Track Variable Changes
        #- **Invariant Variables**:
        #  - `n`: The length of the list `a`, which remains unchanged.
        #  - `first_zero_index`: Remains 0 because the loop only iterates over positions where `a[i]` is 1.
        #  - `first_one_index`: Remains 3 because it was initialized this way and the loop does not update it.
        #  - `a`: The list `a` itself does not change within the loop.
        #- **Variables that Change**:
        #  - `i`: Increases by 1 in each iteration.
        #  - `result`: Grows with each iteration by appending a new string.
        #
        ##### Step 3: Summarize the Loop Behavior
        #- The loop continues as long as `i` is less than `n`.
        #- Each iteration appends `a[i]` to `result` as a string prefixed by `'->'`.
        #- The loop stops when `i` reaches `n`.
        #
        ##### Step 4: Verify Relationships
        #- After the first iteration (`i` becomes 1), `result` becomes `['->0']`.
        #- After the second iteration (`i` becomes 2), `result` becomes `['->0', '->1']`.
        #- After the third iteration (`i` becomes 3), `result` becomes `['->0', '->1', '->0']`.
        #- After the fourth iteration (`i` becomes 4), `result` becomes `['->0', '->1', '->0', '->1']`.
        #
        #Since `n` is 5 and the loop increments `i` until it equals `n`, the loop will execute 4 times in total.
        #
        #### Final Output State
        #- `n` remains 5.
        #- `first_zero_index` remains 0.
        #- `i` will be 4 after the last iteration.
        #- `first_one_index` remains 3.
        #- `a` remains `[1, 0, 1, 0, 1]`.
        #- `result` will contain `['->0', '->1', '->0', '->1', '->0']`.
        #
        #### Output State: 
        #n is 5, first_zero_index is 0, i is 4, first_one_index is 3, a is [1, 0, 1, 0, 1], result is ['->0', '->1', '->0', '->1', '->0']
        print(''.join(result))
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is 5, `a` is a list of integers, and depending on the condition, either the following happens: 
    #- If 0 is in `a` and the number of 1s in the sublist `a[:a.index(0)]` is greater than 0, the result is a list `['->0', '->1', '->0', '->1', '->0']` and a string `'->0->1->0->1->0'` is printed.
    #- If 0 is in `a` but the number of 1s in the sublist `a[:a.index(0)]` is not greater than 0, the same list `a` is maintained and no specific changes or prints are mentioned.
#Overall this is what the function does:The function `func` accepts a list `a` of integers, where each integer is either 0 or 1, and its length `n` satisfies 1 ≤ n ≤ 100,000. The function checks whether there is at least one 0 in the list `a` and ensures that there is at least one 1 before the first 0. If both conditions are met, it constructs a string based on the sequence of 1s and 0s in the list, and prints this string. Otherwise, it prints 'NO'.

