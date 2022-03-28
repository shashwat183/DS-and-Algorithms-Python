def insertion_sort(my_list: list) -> list:
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            # swap
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1

    return my_list


if __name__ == "__main__":
    l = [1, 5, 9, 0, 4, 6, 23, 7, 8, 4, 3]
    print(insertion_sort(my_list=l))
