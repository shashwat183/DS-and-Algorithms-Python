def merge_sort(my_list: list) -> list:
    # Edge case when list has 1 element only
    if len(my_list) == 1:
        return my_list

    list1 = my_list[: int(len(my_list) / 2)]
    list2 = my_list[int(len(my_list) / 2) :]

    if len(list1) > 1:
        list1 = merge_sort(list1)
    if len(list2) > 1:
        list2 = merge_sort(list2)

    return merge(list1=list1, list2=list2)


def merge(list1: list, list2: list) -> list:
    i = 0
    j = 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged


if __name__ == "__main__":
    sorted_l1 = [1, 3, 5, 7]
    sorted_l2 = [2, 7, 9, 11]
    print(merge(list1=sorted_l1, list2=sorted_l2))

    l = [1, 5, 9, 0, 4, 6, 23, 7, 8, 4, 3]
    print(merge_sort(my_list=l))
