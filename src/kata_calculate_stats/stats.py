class Stats:

    def __init__(self):
        pass

    @staticmethod
    def min_value(list_of_num):
        return min(list_of_num)

    @staticmethod
    def max_value(list_of_num):
        return max(list_of_num)

    @staticmethod
    def num_of_elements(list_of_num):
        return len(list_of_num)

    @staticmethod
    def average_value(list_of_num):
        num_of_el = len(list_of_num)
        sum_of_el = sum(list_of_num)
        return round(sum_of_el/num_of_el, 6)
