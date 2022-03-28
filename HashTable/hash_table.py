from typing import List


class HashTable:
    """Hash Table implementation with separate chaining
    for collision handling."""

    def __init__(self, size: int = 7) -> None:
        self.data_map: List[List[str, int]] = [None] * size

    def set(self, key: str, value: int) -> None:
        hash_value = self.__hash(key=key)
        if self.data_map[hash_value] is None:
            self.data_map[hash_value] = []
        self.data_map[hash_value].append([key, value])

    def get(self, key: str):
        hash_value = self.__hash(key=key)
        key_value_pairs = self.data_map[hash_value]
        if key_value_pairs:
            for pair in key_value_pairs:
                if pair[0] == key:
                    return pair[1]

    def keys(self) -> List:
        keys = []
        for map in self.data_map:
            if map:
                for pair in map:
                    keys.append(pair[0])

        return keys

    def items(self):
        items = []
        for map in self.data_map:
            if map:
                for pair in map:
                    items.append(pair)

        return items

    def __hash(self, key: str) -> int:
        hash_value: int = 0
        for letter in key:
            hash_value = (hash_value + ord(letter) * 23) % len(self.data_map)
        return hash_value

    def __str__(self) -> str:
        str_rep = "\n"
        for i in range(len(self.data_map)):
            str_rep += f"{i}: {self.data_map[i]}\n"
        return str_rep


# Using Hash Table(python dict) to find common values between 2 lists
def find_common(list1: List, list2: List):
    temp_dict = {}
    common_values = []
    for value in list1:
        temp_dict[value] = True

    for value in list2:
        if value in temp_dict:
            common_values.append(value)

    return common_values


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.set(key="yolo", value=4)
    hash_table.set(key="polo", value=9)
    hash_table.set(key="shashwat", value=14)
    hash_table.set(key="tolo", value=12)
    hash_table.set(key="kolo", value=92)
    hash_table.set(key="oolo", value=32)
    print(hash_table.get(key="shashwat"))
    print(hash_table.get(key="random"))
    print(hash_table)
    print(hash_table.keys())
    print(hash_table.items())

    print(find_common(list1=[1, 6, 3, 8, 5], list2=[0, 7, 4, 8, 3, 5, 9, 3]))
