#State of the program right berfore the function call: The input string s is a sequence of valid commands consisting of 'L', 'R', lowercase Latin letters, and brackets '(', ')'. The length of the string s is between 1 and 10^6.
def func():
    n = int(input())
    operations = raw_input()
    ans_list = []
    operator_map = {'(': 1, ')': -1}
    left_sum = [(0) for i in xrange(n + 2)]
    right_sum = [(0) for i in xrange(n + 2)]
    left_min = [(0) for i in xrange(n + 2)]
    right_min = [(0) for i in xrange(n + 2)]
    left_max = [(0) for i in xrange(n + 2)]
    right_max = [(0) for i in xrange(n + 2)]
    cursor_pos = 1
    context = [(0) for i in xrange(n + 2)]
    for op in operations:
        if op == 'L':
            cursor_pos = max(1, cursor_pos - 1)
        elif op == 'R':
            cursor_pos += 1
        else:
            op_val = operator_map.get(op, 0)
            context[cursor_pos] = op_val
        
        left_sum[cursor_pos] = left_sum[cursor_pos - 1] + context[cursor_pos]
        
        right_sum[cursor_pos] = right_sum[cursor_pos + 1] + right_sum[cursor_pos]
        
        left_min[cursor_pos] = min(left_min[cursor_pos - 1], context[cursor_pos])
        
        right_min[cursor_pos] = min(right_min[cursor_pos + 1], context[cursor_pos])
        
        left_max[cursor_pos] = max(left_max[cursor_pos - 1], context[cursor_pos])
        
        right_max[cursor_pos] = max(right_max[cursor_pos + 1], context[cursor_pos])
        
        ans = -1
        
        if left_sum[cursor_pos] + right_sum[cursor_pos + 1] == 0 and left_min[
            cursor_pos] >= 0 and right_min[cursor_pos] >= 0:
            ans = max(left_max[cursor_pos], right_max[cursor_pos])
        
        ans_list.append(ans)
        
    #State of the program after the  for loop has been executed: `ans_list` is a list containing the maximum possible values of the right side or left side of the cursor position where the conditions are met (i.e., `left_sum[cursor_pos] + right_sum[cursor_pos + 1] == 0` and both `left_min[cursor_pos]` and `right_min[cursor_pos]` are non-negative), `cursor_pos` is the final position after processing all operations, `left_sum[cursor_pos]` is the cumulative sum of all values from the start to `cursor_pos`, `right_sum[cursor_pos]` is the cumulative sum of all values from `cursor_pos + 1` to the end, `left_min[cursor_pos]` is the minimum value from the start to `cursor_pos`, `right_min[cursor_pos]` is the minimum value from `cursor_pos + 1` to the end, `left_max[cursor_pos]` is the maximum value from the start to `cursor_pos`, `right_max[cursor_pos]` is the maximum value from `cursor_pos + 1` to the end, `context[cursor_pos]` is the last value set for `cursor_pos`, and `context` is a list that records the values at each position throughout the process.
    print(' '.join(map(str, ans_list)))
#Overall this is what the function does:The function processes a string `operations` containing commands 'L' (move left), 'R' (move right), and parentheses '(', ')' which represent numerical values. It calculates and appends to `ans_list` the maximum possible values of the right or left side of the cursor position under specific conditions (i.e., `left_sum[cursor_pos] + right_sum[cursor_pos + 1] == 0` and both `left_min[cursor_pos]` and `right_min[cursor_pos]` are non-negative). After processing all operations, it prints the contents of `ans_list`. The function also maintains several arrays (`left_sum`, `right_sum`, `left_min`, `right_min`, `left_max`, `right_max`, `context`) to keep track of cumulative sums, minimum/maximum values, and current values at each position during the process. If the operations result in invalid conditions, the corresponding `ans` will be -1 and appended to `ans_list`. The function does not handle invalid inputs such as commands other than 'L', 'R', '(', ')', or non-integer values for parentheses. Additionally, the function uses `raw_input()` instead of `input()`, which might lead to a `NameError` in Python 3, as `raw_input()` was renamed to `input()` in Python 3.

