# Challenge: List Sort Using Trie


from Trie import Trie
# TrieNode => {children, is_end_word, char}


def find_words_aux(root, answer, temp):
    if root == None:
        return
    temp += root.char
    if root.is_end_word is True:
        answer.append(temp)
    current = root
    for child in current.children:
        if child is not None:
            find_words_aux(child, answer, temp)
    return


def find_words(root):
    # Write your code here
    answer = []
    temp = ""
    find_words_aux(root,  answer, temp)
    return answer


def sort_list(arr):
    trie = Trie()
    for word in arr:
        trie.insert(word)
    return find_words(trie.root)


if __name__ == '__main__':
    # Input keys (use only 'a' through 'z')
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]

    print(sort_list(keys))
