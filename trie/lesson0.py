# Challenge: Total Number of Words in a Trie
from Trie import Trie
# TrieNode => {children, is_end_word, char}


def total_words(root):
    # Write - Your - Code
    if root == None:
        return 0
    total_word = 0
    if root.is_end_word is True:
        total_word += 1
    current = root
    for child in current.children:
        if child is not None:
            total_word += total_words(child)
    return total_word


if __name__ == '__main__':
    # Input keys (use only 'a' through 'z')
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]

    t = Trie()
    print("Keys to insert: \n", keys)

    # Construct Trie
    for words in keys:
        t.insert(words)
    print(total_words(t.root))
