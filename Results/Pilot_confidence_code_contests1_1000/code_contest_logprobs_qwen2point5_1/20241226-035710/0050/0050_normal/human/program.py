def search_sum(numbers, target, _max, partial=[]):
    s = [0, 0]
    for i in range(len(partial)):
        s[0] += partial[i][0]
        s[1] += partial[i][1]

        if (i + 1 + _max[1]) % 10 == 0:
            s[1] += partial[i][1]

    # check partial sums
    if(len(s) == 2):
        if s[0] <= target:
            if s[1] > _max[0]:
                # add maximum value
                _max[1] = len(partial)
                _max[0] = s[1]

        if s[0] > target:
            return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        search_sum(remaining, target, _max, partial + [n]) 

# get maximum 
def max_turn_damage(l, played, is_double = False):
    _max = [0, played]
    search_sum(l, 3, _max)

    # return values
    return _max

if __name__ == "__main__":
    # get size
    n = int(input())

    # read lists
    result = 0
    played = 0
    for k in range(n):

        # read data
        arr = []
        size = int(input())
        for _ in range(size):
            arr.append([(int(i)) for i in raw_input().split()])

        res = max_turn_damage(arr, played, (k + 1) % 5 == 0)
        result += res[0]
        played += res[1]
    
    # print result
    print(result)