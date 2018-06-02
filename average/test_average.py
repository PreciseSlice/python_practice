import unittest
import average


class TestAverageMethods(unittest.TestCase):

    def test_grades(self):
        self.assertEqual(average.grades, [
                         100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5])

    def test_sum(self):
        score = [10, 10, 10]
        self.assertEqual(average.grades_sum(score), 30)


unittest.main()
