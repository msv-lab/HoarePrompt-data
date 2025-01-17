num_case = int(input())
for i in range(num_case):
    string = input()
    if len(set(string)) == 1:
        print("NO")
    else:
        string_copy = string
        lst = []
        count = 0
        flag = False
        while string != "":
            if string != string[::-1]:
                flag = True
                lst.append(string)
                break
            else:
                flag = False
                appear = []
                index = []
                for i in range(len(string)):
                    if string[i] not in appear:
                        appear.append(string[i])
                        index.append(i+1)
                for i in index:
                    if string[:i] != string[:i][::-1] and len(string[i:]) != 1:
                        flag = True
                        lst.append(string[:i])
                        string = string[i:]
                        break
                if not flag:
                    break
        if flag:
            print("YES")
            print(len(lst))
            print(" ".join(lst))
        else:
            print("NO")
        