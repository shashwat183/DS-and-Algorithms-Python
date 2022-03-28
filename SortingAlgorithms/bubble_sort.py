def bubble_sort(my_list: list) -> list:
    # This first loop goes from last to first element of list.
    # looping from 0 to i in second loop allows us to apply bubble sort
    # on the subset of the list that hasnt been sorted yet. This works because
    # at the end of each iteration through the list, bubble sort pushes the
    # largest item to the end of the top of the unsorted list.
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(0, i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp

    return my_list


if __name__ == "__main__":
    l = [1, 5, 9, 0, 4, 6, 23, 7, 8, 4, 3]
    print(bubble_sort(l))
