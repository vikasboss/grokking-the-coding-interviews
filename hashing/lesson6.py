# Challenge: Word Formation Using a Hash Table

def is_formation_possible(lst, word):
    # Write your code here
    set1 = set(lst)
    n = len(word)
    if (n == 0):
        return True
    for i in range(n):
        if word[:i] in set1 and word[i:] in set1:
            return True
    return False


if __name__ == '__main__':
    lst = ["the", "hello", "there", "answer", "any",
           "by", "world", "their", "abc"]

    word = "helloworld"
    print(is_formation_possible(lst, word))
    print(is_formation_possible(lst, "velle"))
