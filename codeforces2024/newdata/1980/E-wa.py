def check(element):
    if len(element[0]) == 1:
        return "YES"
    else:
        lst_column = []
        for i in range(len(element)):
            lst_column_element = []
            for k in range(len(element[i][0])):
                sum = 0
                for j in range(len(element[i])):
                    sum += element[i][j][k]
                lst_column_element.append(sum)
            lst_column.append(lst_column_element)
        lst_row = []
        for i in range(len(element)):
            lst_row_element = []
            for j in range(len(element[i])):
                sum = 0
                for k in range(len(element[i][j])):
                    sum += element[i][j][k]
                lst_row_element.append(sum)
            lst_row.append(lst_row_element)
        if sorted(lst_row[0]) == sorted(lst_row[1]):
            if sorted(lst_column[0]) == sorted(lst_column[1]):
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
    pass
if __name__ == "__main__":
    number_testcase = int(input())
    matrix = []
    lst = []
    for i in range(number_testcase):
        n, m = map(int, input().split())
        if m == 0 and n == 0:
            lst.append("YES")
            break
        elements = []
        element = []
        for j in range(n):
            element.append(list(map(int, input().split())))
        elements.append(element)
        element = []
        for j in range(n):
            element.append(list(map(int, input().split())))
        elements.append(element)
        matrix.append(elements)

    for i in matrix:
        lst.append(check(i))
    for i in lst:
        print(i)