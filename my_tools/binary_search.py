def binary_search(list, searched_number):
    """Custom binary search function

    :param list: list to search in
    :type list: list
    :param searched_number: number to search for
    :type searched_number: int
    :return: True if item exists ; false otherwise
    :rtype: bool
    """

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
