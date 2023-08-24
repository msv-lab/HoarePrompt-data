def find_possible_values(n, path):
    # check if the number of cells in the path is odd
    if n % 2 == 1:
        return "NO"
    
    # create a dictionary to count the occurrences of each number in the path
    occurrences = {}
    for num in path:
        if num not in occurrences:
            occurrences[num] = 1
        else:
            occurrences[num] += 1
    
    # check if there are any number with odd occurrences
    for num in occurrences:
        if occurrences[num] % 2 == 1:
            return "NO"
    
    # find the maximum number in the path
    max_num = max(path)
    
    # find the divisors of the maximum number (x and y)
    divisors = []
    for i in range(1, int(max_num ** 0.5) + 1):
        if max_num % i == 0:
            divisors.append(i)
            if i != max_num // i:
                divisors.append(max_num // i)
    
    # check if there are any possible values for x and y
    for x in divisors:
        y = max_num // x
        divisible = True
        for num in path:
            if (num - 1) // y != (num - 1) % y:
                divisible = False
                break
        if divisible:
            return "YES\n{} {}".format(x, y)
    
    return "NO"

n = int(input())
path = list(map(int, input().split()))

print(find_possible_values(n, path))