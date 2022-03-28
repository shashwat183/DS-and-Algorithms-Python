def quick_sort(my_list: list, left: int, right: int):
    if left < right:
        swap_index = pivot(my_list=my_list, pivot_index=left, end_index=right)
        quick_sort(my_list=my_list, left=left, right=swap_index - 1)
        quick_sort(my_list=my_list, left=swap_index + 1, right=right)
    return my_list


def pivot(my_list: list, pivot_index: int, end_index: int):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            temp = my_list[i]
            my_list[i] = my_list[swap_index]
            my_list[swap_index] = temp

    temp = my_list[pivot_index]
    my_list[pivot_index] = my_list[swap_index]
    my_list[swap_index] = temp

    return swap_index


if __name__ == "__main__":
    # list1 = [6, 2, 7, 4, 3, 9, 1]
    # print(pivot(my_list=list1, pivot_index=0, end_index=len(list1) - 1))
    # print(list1)
    l = [1, 5, 9, 0, 4, 6, 23, 7, 8, 4, 3]
    print(quick_sort(my_list=l, left=0, right=len(l) - 1))
