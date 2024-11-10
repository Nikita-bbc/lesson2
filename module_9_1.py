def min_(*digits):
    for i in digits:
        return min(i)


def max_(*digits):
    for i in digits:
        return max(i)


def len_(*digits):
    for i in digits:
        return len(i)


def sum_(*digits):
    for i in digits:
        return sum(i)


def sort_(*digits):
    for i in digits:
        i.sort()
        return i


def apply_all_func(int_list, *functions):
    results = dict()
    for i in functions:
        results[i.__name__] = i(int_list)
    return results


print(apply_all_func([6.5, 7, 15.984, 11], max_, min_, sort_))
print(apply_all_func([6, 20, 15, 9], len_, sum_, sort_))
