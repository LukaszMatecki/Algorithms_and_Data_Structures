class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.load_factor_threshold = 10
        self.count = 0
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def _rehash(self, new_size):
        new_table = [[] for _ in range(new_size)]
        for chain in self.table:
            for pair in chain:
                new_index = self._hash(pair[0])
                new_table[new_index].append(pair)
        self.table = new_table
        self.size = new_size

    def insert(self, key, value):
        if self.count / self.size >= self.load_factor_threshold:
            self._rehash(self.size * 2)

        index = self._hash(key)
        chain = self.table[index]

        for pair in chain:
            if pair[0] == key:
                pair[1] = value
                return

        chain.append([key, value])
        self.count += 1
        print(f"Inserted ({key}, {value}) at index {index}")
        self.print_table()

    def find(self, key):
        index = self._hash(key)
        chain = self.table[index]

        for pair in chain:
            if pair[0] == key:
                return pair[1]

        return None

    def remove(self, key):
        index = self._hash(key)
        chain = self.table[index]

        for i, pair in enumerate(chain):
            if pair[0] == key:
                del chain[i]
                self.count -= 1
                print(f"Removed key {key} from index {index}")
                self.print_table()

                if self.size > 10 and self.count / self.size <= 0.2:
                    self._rehash(self.size // 2)
                return

    def print_table(self):
        print("Hash Table (Chaining):")
        for i, chain in enumerate(self.table):
            print(f"[{i}]: {chain}")
        print()


class OpenAddressingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.load_factor_threshold = 0.7
        self.count = 0
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def _rehash(self, new_size):
        new_table = [None] * new_size
        old_size = self.size
        self.size = new_size
        for element in self.table:
            if element is not None:
                index = self._hash(element[0])
                while new_table[index] is not None:
                    index = (index + 1) % new_size
                new_table[index] = element
        self.table = new_table

    def insert(self, key, value):
        if self.count / self.size >= self.load_factor_threshold:
            self._rehash(self.size * 2)

        index = self._hash(key)
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size

        if self.table[index] is None:
            self.count += 1

        self.table[index] = (key, value)
        print(f"Inserted ({key}, {value}) at index {index}")
        self.print_table()

    def find(self, key):
        index = self._hash(key)
        start = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start:
                break
        return None

    def remove(self, key):
        index = self._hash(key)
        start = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                break
            index = (index + 1) % self.size
            if index == start:
                return
        else:
            return

        print(f"\nRemoving key {key} from index {index}")
        self.table[index] = None
        self.count -= 1
        self.print_table()

        next_index = (index + 1) % self.size
        while self.table[next_index] is not None:
            key_to_reinsert = self.table[next_index][0]
            value_to_reinsert = self.table[next_index][1]
            self.table[next_index] = None
            self.count -= 1
            self.insert(key_to_reinsert, value_to_reinsert)
            next_index = (next_index + 1) % self.size

        if self.size > 10 and self.count / self.size <= 0.2:
            self._rehash(self.size // 2)

    def print_table(self):
        print("Hash Table:", end=" ")
        for i, elem in enumerate(self.table):
            print(f"[{i}:{elem}]", end=" ")
        print("\n")


if __name__ == "__main__":

    print("\nTEST: ChainingHashTable")
    chaining = ChainingHashTable()
    chaining.insert(5, "5")
    chaining.insert(11, "11")
    chaining.insert(15, "15")
    chaining.insert(25, "25")
    chaining.insert(35, "35")
    chaining.remove(5)
    chaining.insert(5, "5")

    print("\nTEST: OpenAddressingHashTable")
    open_addressing = OpenAddressingHashTable()
    open_addressing.insert(10, "10")
    open_addressing.insert(17, "17")
    open_addressing.insert(30, "30")
    open_addressing.insert(40, "40")
    open_addressing.insert(50, "50")
    open_addressing.insert(13, "13")
    open_addressing.insert(27, "27")
    print("\n--- TABLE BEFORE REMOVAL ---")
    open_addressing.print_table()
    open_addressing.remove(17)
    open_addressing.remove(30)
    print("\n--- TABLE AFTER REMOVING 17 AND 30 ---")
    open_addressing.print_table()
    open_addressing.insert(20, "20")
    print("\n--- TABLE AFTER INSERTING 20 ---")
    open_addressing.print_table()
