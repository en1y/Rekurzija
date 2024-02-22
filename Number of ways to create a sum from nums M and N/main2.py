import unittest


def a(needed_sum):
    """Counts a number of ways to create sum (needed_sum) from elements that are less than sum (needed_sum).
    needed_sum has to be greater than zero
    num_list stands for range between 1 and needed_sum
    contains b method which has its own docstring"""
    if needed_sum <= 0:
        raise TypeError("needed_sum has to be greater than 0")
    num_list = range(1, needed_sum)
    
    def b(identificator, new_sum):
        """Recursive function that will call itself until it won't check every possible sum
        Recursion will go on until the identificator is -1, and then it will check if the new_sum is zero, if it is it will return 1 in the other case it will return 0
        If the new_sum subtracted by num_list[identificator] is greater than 0 it will return itself with the use of the num_list[identificator] and without it, so we can look at all the possibilities
        If the new_sum subtracted by num_list[identificator] is smaller than 0 it will return itself with decreased identificator"""
        if identificator == -1 and new_sum == 0:
            return 1
        if identificator == -1 and new_sum != 0:
            return 0
        if new_sum == num_list[identificator]:
            if identificator >= 1:
                return 1 + b(identificator - 1, new_sum)
            else:
                return 1
        if new_sum - num_list[identificator] > 0:
            return b(identificator-1, new_sum - num_list[identificator]) + b(identificator-1, new_sum)
        else:
            return b(identificator-1, new_sum)
    return b(len(num_list) - 1, needed_sum)


class TestFunction(unittest.TestCase):

    def test_a(self):
        self.assertEqual(a(1), 0)
        self.assertEqual(a(2), 0)
        self.assertEqual(a(3), 1)
        self.assertEqual(a(4), 1)
        self.assertEqual(a(5), 2)
        self.assertEqual(a(6), 3)
        self.assertEqual(a(7), 4)
        self.assertEqual(a(8), 5)
        self.assertEqual(a(9), 7)
        self.assertEqual(a(10), 9)


# print(a(9))


if __name__ == '__main__':
     unittest.main()

