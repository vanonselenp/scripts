import unittest


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


class IsLeapYearShould(unittest.TestCase):
    def test_output_false_for_year_one(self):
        self.assertEquals(is_leap_year(1), False)

    def test_output_false_for_year_not_divisible_by_four(self):
        self.assertEquals(is_leap_year(3), False)

    def test_output_true_for_year_4(self):
        self.assertEquals(is_leap_year(4), True)

    def test_output_true_for_year_8(self):
        self.assertEquals(is_leap_year(8), True)

    def test_output_true_for_year_12(self):
        self.assertEquals(is_leap_year(12), True)
    
    def test_output_false_for_year_divisible_by_100(self):
        self.assertEquals(is_leap_year(100), False)

    def test_output_false_for_year_divisible_by_200(self):
        self.assertEquals(is_leap_year(200), False)

    def test_output_false_for_year_divisible_by_300(self):
        self.assertEquals(is_leap_year(300), False)

    def test_output_true_for_year_divisible_by_400(self):
        self.assertEquals(is_leap_year(400), True)

    def test_output_true_for_year_divisible_by_800(self):
        self.assertEquals(is_leap_year(800), True)

    def test_output_true_for_year_divisible_by_1200(self):
        self.assertEquals(is_leap_year(1200), True)

    def test_output_false_for_2001(self):
        self.assertEquals(is_leap_year(2001), False)

    def test_output_true_for_year_2000(self):
        self.assertEquals(is_leap_year(2000), True)


if __name__ == "__main__":
    unittest.main()
