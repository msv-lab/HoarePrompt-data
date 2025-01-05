test_cases = int(input())
for n in range(test_cases):
    path_size = int(input())
    path = input()
    coin_counter = 0
    position = 0
    while position != path_size - 1:
        if path[position + 1] == '*':
            if position < path_size - 2:
                if path[position + 2] == '*':
                    break
                else:
                    if path[position + 2] == '@':
                        coin_counter +=1
                    position += 2
            else:
                break
        else:
            if path[position + 1] == '@':
                coin_counter += 1
                position += 1
            elif position < path_size - 2:
                if path[position + 2] != '*':
                    position += 2
                else:
                    position += 1
            else:
                break

    print(coin_counter)