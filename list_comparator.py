class ListComparator:


    # pip install pylint
    # pylint list_comparator.py > pylint_report.txt

    # pytest test_list_comparator.py
    # coverage run - m
    # pytest test_list_comparator.py
    # coverage  report - m

    def find_average(self, nums):
        return sum(nums) / len(nums)

    def compare_lists(self, list1, list2):
        average1 = self.find_average(list1)
        average2 = self.find_average(list2)

        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average1 < average2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
