def binary_search(list, searched_number):
    st = 0
    dr = len(list) - 1

    while st <= dr:
        m = (st + dr) // 2
        if list[m] == searched_number:
            return True
        if list[m] < searched_number:
            st = m + 1
        else:
            dr = m - 1
    return False

