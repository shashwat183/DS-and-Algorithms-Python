def bubble_sort(my_list: list):
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
