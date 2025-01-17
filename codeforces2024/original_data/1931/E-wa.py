def countZero(number):
    counter = 0
    for i in range(len(number)-1, 0, -1):
        if (number[i] != '0'):
            break;
        counter += 1
    return counter

def anna(arr):
    idx = 0
    found = True if arr[0][-1] == '0' else False

    for i in range(1, len(arr)):
        if arr[i][-1] == '0':
            if countZero(arr[i]) > countZero(arr[idx]):
                found = True
                idx = i

    if found:
        arr[idx] = str(int(arr[idx][::-1]))

    return arr          # if no ele with 0 at end is found, then we return same arr

def sasha(arr):
    idx1 = 0
    foundOne = False
    idx2 = 0
    for i in range(1, len(arr)):
        if arr[i][-1] == '0':
            if countZero(arr[i]) > countZero(arr[idx1]):
                foundOne = True
                idx1 = i
    for i in range(1, len(arr)):
        if i !=idx1 and arr[i][-1] == '0':
            if countZero(arr[i]) >= countZero(arr[idx2]):
                idx2 = i

    if (idx2 != 0):    
        # print(f"Two 0s found at {{ {idx1} }} and {{ {idx2} }}.")
        if countZero(arr[idx1]) > countZero(arr[idx2]):         # The one with less zeros at end would be after more zeros
            arr[idx1] = arr[idx1] + arr[idx2]
        else:
            arr[idx1] = arr[idx2] + arr[idx1]
        arr.pop(idx2)
    
    elif foundOne and idx2 == 0 :
        for i in range(1, len(arr)):
            if len(arr[i]) > len(arr[idx2]):
                idx2 = i
        # print(f"Only one 0 found at {{ {idx1} }} other chosen {{ {idx2} }}")
        arr[idx1] = arr[idx1] + arr[idx2]
        arr.pop(idx2)

    else:
        # print(f"No zeros found, so just adding the firsttwo; ")
        arr[0] = arr[0] + arr[1]
        arr.pop(1)

    return arr

def play(arr, n, m):
    if (n > m):
        return "Sasha"
    elif (n == m):
        flag1 = False
        flag2 = False
        for i in range(n):
            if (flag2 == False and len(arr[i]) >= 2):
                if (flag1 == False):
                    flag1 = True
                    if (len(arr[i]) > 2) or (arr[i][-1] != '0'):
                        flag2 = True
                else:
                    flag2 = True
        if (flag2):
            return "Sasha"
        else:
            return "Anna"
    else:
        # print(f"Starting with {arr}")
        while (len(arr) > 1):
            arr = anna(arr)
            # print(f"Anna did {arr}")
            arr = sasha(arr)
            # print(f"Sasha did {arr}")

        if (int(arr[0]) >= 10**m):
            return "Sasha"
        else:
            return "Anna"

# Sasha wants BIG
# Anna wants smol

t = int(input())
for testcase in range(t):
    n,m = map(int, input().split())    
    a = input().split(' ')

    print(play(a, n, m))