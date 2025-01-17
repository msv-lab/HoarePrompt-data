def is_sublist(main_list, sub_list):
    return sub_list in [main_list[i:i+len(sub_list)] for i in range(len(main_list)-len(sub_list)+1)]