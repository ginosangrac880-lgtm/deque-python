import numpy as np
from deque_interface import DequeInterface


class deque(DequeInterface):

    def __init__(self, arraySize: int) -> None:

        self.arraySize = arraySize

        self.myArray = np.empty(arraySize, dtype=np.int32)

        self.head = 0
        self.size = 0


    def accessByIndex(self, index: np.int32) -> np.int32:

        if index < 0 or index >= self.size:
            raise IndexError("Такого элемента нет")

        realIndex = (self.head + int(index)) % self.arraySize

        return self.myArray[realIndex]


    def addToTail(self, num: np.int32) -> np.int32:

        if self.size >= self.arraySize:
            raise OverflowError("Deque заполнен")

        tailIndex = (self.head + self.size) % self.arraySize

        self.myArray[tailIndex] = num

        self.size += 1

        return np.int32(0)


    def addToHead(self, num: np.int32) -> np.int32:

        if self.size >= self.arraySize:
            raise OverflowError("Deque заполнен")

        self.head = (self.head - 1) % self.arraySize

        self.myArray[self.head] = num

        self.size += 1

        return np.int32(0)



# Проверка работы deque
if __name__ == "__main__":

    d = deque(5)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))
    d.addToTail(np.int32(30))

    print(d.arraySize)

    for i in range(d.size):
        print(d.accessByIndex(i))