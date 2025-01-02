n = int(input())
operations = raw_input()
ans_list = []
operator_map = {'(': 1, ')': -1}
left_sum = [0 for i in xrange(n + 2)]
right_sum = [0 for i in xrange(n + 2)]
left_min = [0 for i in xrange(n + 2)]
right_min = [0 for i in xrange(n + 2)]
left_max = [0 for i in xrange(n + 2)]
right_max = [0 for i in xrange(n + 2)]
cursor_pos = 1
context = [0 for i in xrange(n + 2)]
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
    if left_sum[cursor_pos] + right_sum[cursor_pos + 1] == 0 and left_min[cursor_pos] >= 0 and (right_min[cursor_pos] >= 0):
        ans = max(left_max[cursor_pos], right_max[cursor_pos])
    ans_list.append(ans)
print(' '.join(map(str, ans_list)))