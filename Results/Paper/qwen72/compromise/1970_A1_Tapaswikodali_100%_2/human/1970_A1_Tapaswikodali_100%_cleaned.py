class BalanceInfo:

    def __init__(self, balance, position, character):
        self.balance = balance
        self.position = position
        self.character = character

def func_1(infoA, infoB):
    if infoA.balance != infoB.balance:
        return infoA.balance - infoB.balance
    return infoB.position - infoA.position

def func_2(s):
    n = len(s)
    balance_info = []
    balance = 0
    for i in range(n):
        balance_info.append(BalanceInfo(balance, i, s[i]))
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1
    balance_info.sort(key=lambda x: (x.balance, -x.position))
    result = ''.join((info.character for info in balance_info))
    print(result)
if __name__ == '__main__':
    s = input().strip()
    func_2(s)