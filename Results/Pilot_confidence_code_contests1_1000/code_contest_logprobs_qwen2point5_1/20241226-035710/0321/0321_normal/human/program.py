import sys


def main(arr):
    if len(arr) == 1:
        return 1

    arr.sort()
    start = 0
    move = len(arr) // 2
    ans = len(arr)
    while move < len(arr):
        if arr[start] is None:
            move += 1
        elif arr[start] * 2 > arr[move]:
            # Try to find a match for start.
            move += 1
        else:
            # Can do a grouping.
            arr[move] = None
            ans -= 1
            move += 1
            start += 1
    return ans


if __name__ == "__main__":
    arr = []
    for e, line in enumerate(sys.stdin.readlines()):
        if e == 0:
            continue
        arr.append(int(line.strip()))
    print(main(arr))
