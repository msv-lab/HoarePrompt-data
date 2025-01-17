n = int(input())
args = list(map(int, input().split()))
def can_imply_false(args):
    if len(args) == 1:
        return args[0] == 0
    for i in range(len(args) - 1):
        if args[i] == 1 and args[i + 1] == 0:
            new_args = args[:i] + [0] + args[i + 2:]
            if can_imply_false(new_args):
                return True
    return False

if can_imply_false(args):
    print("YES")
    brackets = []
    for arg in args:
        if brackets and brackets[-1][0] == 1 and arg == 0:
            brackets[-1][1] = ')'
            brackets.append('(')
        brackets.append(str(arg))
        if brackets[-2][0] == 1 and arg == 0:
            brackets.append(')')
    print('->'.join(brackets))
else:
    print("NO")
