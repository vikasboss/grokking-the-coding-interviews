# Challenge: Find All Words Stored in Trie

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


if __name__ == '__main__':
    # Input keys (use only 'a' through 'z')
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]

    t = Trie()
    print("Keys to insert: \n", keys)

    # Construct Trie
    for words in keys:
        t.insert(words)
    print(find_words(t.root))
