def permutations(n):
    results = []

    def inner(current_permutation):
        if len(current_permutation) == n:
            results.append(current_permutation)
            return

        for i in range(1, n + 1):
            if i not in current_permutation:
                inner(current_permutation + [i])

    inner([])
    return results


def permutation_list(list):
    n = len(list)
    return permutations(n)


def minus_one(list):
    new_list = []
    for onj in permutation_list(list):
        intermediate_list = []
        for i in range(len(onj)):
            intermediate_list.append(onj[i] - 1)
        new_list.append(intermediate_list)
    return new_list


def elements_of_list(list):
    new_list = []
    for obj in minus_one(list):
        intermediate_list = []
        for i in obj:
            intermediate_list.append(list[i])
        new_list.append(intermediate_list)
    return new_list


