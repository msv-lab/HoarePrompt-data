def biggest_num(lis):
    return max(lis)

def first_index_swap(lis, my_cow_index):
    shadow_list = lis[:]
    a = shadow_list[0]
    shadow_list[0] = lis[my_cow_index]
    shadow_list[my_cow_index] = a
    return shadow_list

def first_max_index_swap(lis, my_cow_index, max_index):
    shadow_list = lis[:]
    a = shadow_list[max_index]
    shadow_list[max_index] = lis[my_cow_index]
    shadow_list[my_cow_index] = a
    return shadow_list

t = int(input())  # input the number of test cases
cows_and_its_index = []
cows_values = []
simultaneous_wins_list_mine = []
simultaneous_wins_list_other = []
simultaneous_wins_final_list = []

cows_greater_than_mine = []
simultaneous_wins_from_first = []
simultaneous_wins_from_first_max = []

for i in range(0, t):
    x = input().split()  # input the list of cows and their index
    for j in range(0, len(x)):
        x[j] = int(x[j])
        cows_and_its_index.append(x[j])

    y = input().split()  # input the values of the cows
    for j in range(0, len(y)):
        y[j] = int(y[j])
        cows_values.append(y[j])

    my_cow_index = cows_and_its_index[1] - 1  # Convert to 0-based index
    if my_cow_index < 0 or my_cow_index >= len(cows_values):
        simultaneous_wins_final_list.append(0)
        continue

    max_num = biggest_num(cows_values)

    for k in range(0, len(cows_values)):
        if cows_values[my_cow_index] < cows_values[k]:
            cows_greater_than_mine.append(cows_values[k])

    if not cows_greater_than_mine:
        simultaneous_wins_final_list.append(0)
        cows_and_its_index.clear()
        cows_values.clear()
        continue

    # First index swap
    shadow_list = first_index_swap(cows_values, my_cow_index)
    simultaneous_wins = 0
    for k in range(0, len(cows_values)):
        if shadow_list[0] > cows_values[k]:
            simultaneous_wins += 1
        elif shadow_list[0] < cows_values[k]:
            break
    simultaneous_wins_from_first.append(simultaneous_wins)

    # First max index swap
    max_index = cows_values.index(cows_greater_than_mine[0])
    shadow_list = first_max_index_swap(cows_values, my_cow_index, max_index)
    simultaneous_wins = 0
    for k in range(max_index, len(cows_values)):
        if shadow_list[max_index] > cows_values[k]:
            simultaneous_wins += 1
        elif shadow_list[max_index] < cows_values[k]:
            break
    simultaneous_wins_from_first_max.append(simultaneous_wins)

    simultaneous_wins_final_list.append(
        max(simultaneous_wins_from_first[0], simultaneous_wins_from_first_max[0])
    )

    # Clear lists for next test case
    simultaneous_wins_from_first.clear()
    simultaneous_wins_from_first_max.clear()
    cows_greater_than_mine.clear()
    cows_and_its_index.clear()
    cows_values.clear()

for i in range(0, len(simultaneous_wins_final_list)):
    print(simultaneous_wins_final_list[i])
