def get_distinct_list(list1, list2):
    """
    Временная сложность O(nm), где n - число элементов list1, m - число элементов list2.
    Пространственная сложность O(n) в худшем случае, если list1 и list2 не пересекаются. Здесь опущен
    размер пустого списка из предположения, что число элементов и их размер в list1 достаточно большие,
    т.е. взята нижняя граница для худшего случая.
    """
    return [item for item in list1 if item not in list2]


if __name__ == '__main__':
    l1 = [1, 3, 6, 4]
    l2 = [2, 3]
    expected = [1, 6, 4]

    assert get_distinct_list(l1, l2) == expected
