def remove_zero(list_):
    """
    python уже выделил память под объекты 0 и 1.
    Дополнительно выделяется память только под i.
    Пространственная сложность O(1).
    """
    i = len(list_) - 1
    while i >= 0:
        if not list_[i]:
            del list_[i]
        i -= 1


if __name__ == '__main__':
    input_ = [0, 0, 1, 0, 2, 3, -1, 0, 0, 4]
    expected = [1, 2, 3, -1, 4]
    remove_zero(input_)

    assert input_ == expected
