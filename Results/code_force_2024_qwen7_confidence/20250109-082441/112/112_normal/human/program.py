def convert(lst):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic = dict()
    s = ""
    for i in lst:
        if i == 0:
            dic[alphabet[i]] = 0
            s += alphabet[i]
            alphabet.pop(0)
            continue
        else:
            for key, value in dic.items():
                if value == i - 1:
                    dic[key] += 1
                    s += key
                    break
    return s
if __name__ == "__main__":
    t = int(input())
    lst_string = []
    for i in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        lst_string.append(convert(lst))
    for i in lst_string:
        print(i)