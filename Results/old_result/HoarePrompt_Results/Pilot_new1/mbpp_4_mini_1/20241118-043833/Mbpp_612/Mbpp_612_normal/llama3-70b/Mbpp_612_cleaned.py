def func_1(list_of_lists):
    return [list((element[0] for element in list_of_lists)), list((element[1] for element in list_of_lists))]