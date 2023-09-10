# Challenge: Word Formation From a Dictionary Using Trie


from Trie import Trie
# TrieNode => {children, is_end_word, char}


def checkWordBreak(root, strr):
    n = len(strr)
    if (n == 0):
        return True
    for i in range(1, n+1):
        if (root.search(strr[:i])
                and root.search(strr[i:])):
            return True
    return False


def is_formation_possible(dictionary, word):
    # Write your code here
    trie = Trie()
    for single_word in dictionary:
        trie.insert(single_word)
    return checkWordBreak(trie, word)


if __name__ == '__main__':
    # Input keys (use only 'a' through 'z')
    dictionary = ["the", "hello", "there", "answer",
                  "any", "by", "world", "their", "abc"]
    word = "helloworld"
    print(is_formation_possible(dictionary, word=word))
