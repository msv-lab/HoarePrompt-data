def is_Sub_Array(main_list, sub_list):
    return ''.join(map(str, sub_list)) in ''.join(map(str, main_list))
