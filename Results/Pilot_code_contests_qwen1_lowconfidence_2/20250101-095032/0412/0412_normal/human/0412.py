#encoding: utf-8
read_input = map(int, raw_input().split())

n = read_input[0]
d = read_input[1]

input_list = []

for i in range(n):
    user_input = map(int, raw_input().split())
    input_list.append((user_input[0], user_input[1]))

input_list.sort()

max_factor = input_list[0][1]
partial_sum = input_list[0][1]

j = 0
for i in range(1, n):
    while((input_list[i][0] - input_list[j][0]) >= d):
        partial_sum -= input_list[j][1]
        j += 1

    partial_sum += input_list[i][1]
    max_factor = max(max_factor, partial_sum)

print(max_factor)