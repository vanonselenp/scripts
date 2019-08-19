# Agile Distilled code katas actioning. 
import unittest


def fizz_buzz(number):
    output = ""
    if number % 3 == 0:
        output += "fizz"
    if number % 5 == 0:
        output += "buzz"
    return output or str(number)


class FizzShould(unittest.TestCase):
    def test_output_string_number_when_call_with_one(self):
        self.assertEquals(fizz_buzz(1), "1")

    def test_output_string_number_when_call_with_two(self):
        self.assertEquals(fizz_buzz(2), "2")

    def test_output_string_number_when_call_with_four(self):
        self.assertEquals(fizz_buzz(4), "4")

    def test_output_fizz_when_fizz_with_three(self):
        self.assertEquals(fizz_buzz(3), "fizz")

    def test_output_fizz_when_fizz_with_six(self):
        self.assertEquals(fizz_buzz(6), "fizz")
    
    def test_output_fizz_when_fizz_with_nine(self):
        self.assertEquals(fizz_buzz(9), "fizz")

    def test_output_buzz_when_fizz_with_five(self):
        self.assertEquals(fizz_buzz(5), "buzz")

    def test_output_buzz_when_fizz_with_ten(self):
        self.assertEquals(fizz_buzz(10), "buzz")

    def test_output_buzz_when_fizz_with_twenty(self):
        self.assertEquals(fizz_buzz(20), "buzz")

    def test_output_fizzbuzz_when_fizz_with_15(self):
        self.assertEquals(fizz_buzz(15), "fizzbuzz")

    def test_output_fizzbuzz_when_fizz_with_30(self):
        self.assertEquals(fizz_buzz(30), "fizzbuzz")

    def test_output_fizzbuzz_when_fizz_with_45(self):
        self.assertEquals(fizz_buzz(45), "fizzbuzz")


if __name__ == "__main__":
    unittest.main()