def find_possible_values(n, path):
    # create a dictionary to count the occurrences of each number from 1 to the maximum number in the path (inclusive)
    occurrences = {}
    for num in path:
        for i in range(1, num + 1):
            if i not in occurrences:
                occurrences[i] = 0
        occurrences[num] += 1

    # check if there are any number with odd occurrences
    for num in occurrences:
        if occurrences[num] % 2 == 1:
            return "NO"

    # find the maximum number in the path
    max_num = max(path)

    # iterate through each number from 1 to the maximum number in the path (inclusive)
    for num in range(1, max_num + 1):
        # find the divisors of the current number (x and y)
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)

        # check if there are any possible values for x and y
        for x in divisors:
            y = num // x
            divisible = True
            for i in range(1, num + 1):
                # calculate the row and column indices based on the values of x and y
                row = (i - 1) // y + 1
                col = (i - 1) % y + 1
                # check if the current number can be placed in the matrix based on the calculated indices
                if path[i - 1] != (row - 1) * y + col:
                    divisible = False
                    break
            if divisible:
                return "YES\n{} {}".format(x, y)

    return "NO"

n = int(input())
path = list(map(int, input().split()))

print(find_possible_values(n, path))