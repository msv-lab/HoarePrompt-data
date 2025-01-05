from sys import stdin


def solve(a):
    stack, ans = [], 0
    for i in a:
        while stack and stack[-1] < i:
            stack.pop()

        stack.append(i)
        if len(stack) > 1:
            ans = max(ans, stack[-1] ^ stack[-2])

    return ans


n, a = int(input()), [int(x) for x in stdin.readline().split()]
print(solve(a))