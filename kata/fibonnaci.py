import unittest


def fib(position):
    if position == 1 or position == 0:
        return position

    return fib(position - 1) + fib(position - 2)


class FibShould(unittest.TestCase):
    def test_return_0_for_position_0(self):
        self.assertEquals(fib(0), 0)

    def test_return_1_for_position_1(self):
        self.assertEquals(fib(1), 1)

    def test_return_1_for_position_2(self):
        self.assertEquals(fib(2), 1)

    def test_return_2_for_position_3(self):
        self.assertEquals(fib(3), 2)

    def test_return_3_for_position_4(self):
        self.assertEquals(fib(4), 3)

    def test_return_5_for_position_5(self):
        self.assertEquals(fib(5), 5)

    def test_return_8_for_position_6(self):
        self.assertEquals(fib(6), 8)


if __name__ == "__main__":
    unittest.main()