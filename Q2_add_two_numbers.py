
l1 = [1, 2, 3]
l2 = [4, 5, 6]

new_l1 = [str(l1[len(l1) - index - 1]) for index in range(len(l1))]
new_l2 = [str(l2[len(l1) - index - 1]) for index in range(len(l2))]
str_l1 = "".join(new_l1)
str_l2 = "".join(new_l2)
int_l1 = int(str_l1)
int_l2 = int(str_l2)
result = str(int_l1 + int_l2)
result_list = list(result)
print([result_list[len(result_list) - index -1] for index in range(len(result_list))])
