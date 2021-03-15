def my_sorted(list, key=None, reverse=False):
    new_list = list[:]
    for i in range(len(new_list) - 1):
        for j in range(i + 1, len(new_list)):
            first_element = new_list[i]
            second_element = new_list[j]
            if key is not None:
                first_element = key(first_element)
                second_element = key(second_element)
            condition = first_element > second_element
            if reverse:
                condition = not condition
            if condition:
                auxiliary = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = auxiliary
    return new_list
