import pytest
from list_comparator import ListComparator

comparator = ListComparator()

def test_compare_lists_first_greater():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3]
    assert comparator.compare_lists(list1, list2) == "Первый список имеет большее среднее значение"

def test_compare_lists_second_greater():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3, 4, 5]
    assert comparator.compare_lists(list1, list2) == "Второй список имеет большее среднее значение"

def test_compare_lists_equal():
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]
    assert comparator.compare_lists(list1, list2) == "Средние значения равны"
