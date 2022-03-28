class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next = []


def string_diff_by_1(str1, str2):
    if len(str1) == len(str2):
        first_diff_spotted = False
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                if first_diff_spotted:
                    return False
                else:
                    first_diff_spotted = True
    if not first_diff_spotted:
        return False
    return True


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        def generate_tree(begin_word, end_word, word_list):
            if end_word not in word_list:
                return None
            root = TreeNode(val=begin_word)
            ended = False
            queue = [[root]]
            ended = False
            for level in queue:
                next_level = []
                for element in level:
                    print(element.val)
                    for word in word_list:
                        if string_diff_by_1(word, element.val):
                            node = TreeNode(val=word)
                            element.next.append(node)
                            next_level.append(node)
                            if word == end_word:
                                ended = True
                if not ended:
                    queue.append(next_level)

            return root

        root_node = generate_tree(
            begin_word=beginWord, end_word=endWord, word_list=wordList
        )

        print(root_node.next)
        return []
