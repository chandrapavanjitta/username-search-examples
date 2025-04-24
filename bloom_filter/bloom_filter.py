import hashlib


class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size
        self.item_count = 0  # Initialize item counter

    def _hashes(self, item):
        for i in range(self.hash_count):
            hash_result = int(hashlib.md5((item + str(i)).encode()).hexdigest(), 16)
            yield hash_result % self.size

    def add(self, item):
        is_potentially_present = self.check(item)  # Check before setting bits
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

        if not is_potentially_present:
            # Increment item count only if the item was not already present
            self.item_count += 1

    def check(self, item):
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))

    def count(self):
        """
        Returns the number of items added to the filter.
        """
        return self.item_count
