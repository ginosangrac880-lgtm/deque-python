import numpy as np
from deque import deque


def test_add_to_tail():
    d = deque(5)

    d.addToTail(np.int32(7))
    d.addToTail(np.int32(14))
    d.addToTail(np.int32(21))

    assert d.accessByIndex(0) == 7
    assert d.accessByIndex(1) == 14
    assert d.accessByIndex(2) == 21

    print("test_add_to_tail пройден")


def test_add_to_head():
    d = deque(5)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))
    d.addToHead(np.int32(5))

    assert d.accessByIndex(0) == 5
    assert d.accessByIndex(1) == 10
    assert d.accessByIndex(2) == 20

    print("test_add_to_head пройден")


def test_head_and_tail():
    d = deque(6)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))

    d.addToHead(np.int32(5))
    d.addToHead(np.int32(2))

    assert d.accessByIndex(0) == 2
    assert d.accessByIndex(1) == 5
    assert d.accessByIndex(2) == 10
    assert d.accessByIndex(3) == 20

    print("test_head_and_tail пройден")


def test_overflow():
    d = deque(3)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))
    d.addToTail(np.int32(30))

    try:
        d.addToTail(np.int32(40))

        assert False

    except OverflowError:
        print("test_overflow пройден")


def test_wrong_index():
    d = deque(4)

    d.addToTail(np.int32(11))
    d.addToTail(np.int32(22))

    try:
        d.accessByIndex(5)

        assert False

    except IndexError:
        print("test_wrong_index пройден")


def test_circle():
    d = deque(3)

    d.addToHead(np.int32(30))
    d.addToHead(np.int32(20))
    d.addToHead(np.int32(10))

    assert d.accessByIndex(0) == 10
    assert d.accessByIndex(1) == 20
    assert d.accessByIndex(2) == 30

    print("test_circle пройден")


test_add_to_tail()
test_add_to_head()
test_head_and_tail()
test_overflow()
test_wrong_index()
test_circle()

print("Все тесты успешно пройдены!")