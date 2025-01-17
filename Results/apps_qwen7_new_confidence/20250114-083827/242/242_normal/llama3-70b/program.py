n, m, min_val, max_val = map(int, input().split())
temp = list(map(int, input().split()))

if min_val in temp and max_val in temp:
    print('Correct')
else:
    if min_val not in temp and max_val not in temp:
        if min_val < min(temp) or max_val > max(temp):
            print('Incorrect')
        else:
            print('Correct')
    else:
        print('Incorrect')
