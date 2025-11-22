class LinearProbingTable:

    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    class _Tomb:
        pass

    TOMBSTONE = _Tomb()

    def __init__(self, capacity=32):
        self._cap = capacity
        self._table = [None] * capacity
        self._size = 0

    def __len__(self):
        return self._size

    def capacity(self):
        return self._cap

    def _index(self, key):
        return hash(key) % self._cap

    def _load_factor(self):
        return self._size / self._cap

    def _rehash(self):
        old = self._table
        self._cap *= 2
        self._table = [None] * self._cap
        old_size = self._size
        self._size = 0

        for slot in old:
            if isinstance(slot, self.Record):
                self.insert(slot.key, slot.value)

        self._size = old_size

    def insert(self, key, value):
        idx = self._index(key)
        first_tomb = None
        start = idx

        while True:
            slot = self._table[idx]

            if slot is None:
                insert_idx = first_tomb if first_tomb is not None else idx
                self._table[insert_idx] = self.Record(key, value)
                self._size += 1
                if self._load_factor() > 0.7:
                    self._rehash()
                return True

            if slot is self.TOMBSTONE:
                if first_tomb is None:
                    first_tomb = idx

            elif slot.key == key:
                return False

            idx = (idx + 1) % self._cap
            if idx == start:
                return False

    def search(self, key):
        idx = self._index(key)
        start = idx

        while True:
            slot = self._table[idx]

            if slot is None:
                return None
            if slot is not self.TOMBSTONE and slot.key == key:
                return slot.value

            idx = (idx + 1) % self._cap
            if idx == start:
                return None

    def modify(self, key, value):
        idx = self._index(key)
        start = idx

        while True:
            slot = self._table[idx]

            if slot is None:
                return False
            if slot is not self.TOMBSTONE and slot.key == key:
                slot.value = value
                return True

            idx = (idx + 1) % self._cap
            if idx == start:
                return False

    def remove(self, key):
        idx = self._index(key)
        start = idx

        while True:
            slot = self._table[idx]

            if slot is None:
                return False
            if slot is not self.TOMBSTONE and slot.key == key:
                self._table[idx] = self.TOMBSTONE
                self._size -= 1
                return True

            idx = (idx + 1) % self._cap
            if idx == start:
                return False
