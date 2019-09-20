
# The first version, high memory usage and high runtime
def reverse(x):
    x_str = str(x)
    length = len(x_str)
    new_str_list = []
    if x_str[0] == "-":
        new_str_list.append("-")
        length -= 1
    for num in (range(length)):
        new_str_list.append(x_str[-num - 1])
    new_num = int("".join(new_str_list))
    result = int(new_num)
    if abs(result) > 2147483647:
        return 0
    else:
        return result


# A much more faster version
def reverse(x):
    x = str(x)
    if x[0] == "-":
        new_str_list = []
        new_str_list.append("-")
        for num in (range(len(x) - 1)):
            new_str_list.append(x[-num - 1])
    else:
        new_str_list = [x[-num - 1] for num in range(len(x))]
    x = int("".join(new_str_list))
    if abs(x) > 2147483647:
        return 0
    return x
