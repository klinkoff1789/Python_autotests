li_1 = [1, 8, 3]
li_2 = [2, 4, 6, 7]

[1, 2, 8, 4, 3, 6, 7]


def merge_list(li_1, li_2):
    new_li = []
    if len(li_1) <= len(li_2):
        min_len = len(li_1)
    else:
        min_len = len(li_2)
    for i in range(min_len):
        print(min_len)
        try:
            new_li.append(li_1[i])
            new_li.append(li_2[i])
        except IndexError as e:
            print(e)
    new_li.extend(li_2[min_len:])
    return new_li


print(merge_list(li_1, li_2))