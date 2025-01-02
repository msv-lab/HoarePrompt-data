input_value = int(input())

value_class = [3, 0, 2, 1]
value_label = ["A", "B", "C", "D"]

def value_num(n):
    return value_class[n % 4]

top_value = value_num(input_value)
top_add = 0
for add in [1, 2]:
    add_val = value_num(input_value + add)
    if add_val < top_value:
        top_add = add
        top_value = add_val
print( str(top_add) + " " + value_label[top_value] )
