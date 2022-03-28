def selection_sort(my_list: list) -> list:
    for i in range(0, len(my_list) - 1):
        min_index = i
        for j in range(i, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    return my_list


if __name__ == "__main__":
    l = [1, 5, 9, 0, 4, 6, 23, 7, 8, 4, 3]
    print(selection_sort(my_list=l))
