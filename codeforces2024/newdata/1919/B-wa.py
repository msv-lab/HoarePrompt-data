test_count = input()
for t in range(int(test_count)):
    string_len = input()
    string = input()
    run_sum = 0
    for s in string:
        val = s == '+'
        run_sum += 1 * val + -1 * (not val)
    print(run_sum)

