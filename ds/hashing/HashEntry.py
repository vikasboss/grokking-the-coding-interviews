class HashEntry:
    def __init__(self, key, data):
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.nxt = None

    def __str__(self):
        return str(entry.key) + ", " + entry.value


if __name__ == '__main__':
    entry = HashEntry(3, "Educative")
    print(entry)
