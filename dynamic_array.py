class DynamicArray:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()

        self.array[self.size] = value
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        return self.array[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        self.array[index] = value

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1

    def _resize(self):
        self.capacity *= 2

        new_array = [None] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array

    def __len__(self):
        return self.size
