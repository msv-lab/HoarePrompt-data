(n, m, min_temp, max_temp) = map(int, input().split())
temperatures = list(map(int, input().split()))
contains_min = min_temp in temperatures
contains_max = max_temp in temperatures
additional_needed = n - m
if contains_min and contains_max:
    print('Correct')
elif additional_needed >= 2 or (additional_needed == 1 and (contains_min or contains_max)):
    print('Correct')
else:
    print('Incorrect')