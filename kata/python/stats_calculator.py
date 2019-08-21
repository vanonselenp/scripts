import unittest


def stats_calculator(input):
    min_value = input[0]
    max_value = min_value
    total = min_value

    for i in range(1, len(input)):
        if min_value > input[i]:
            min_value = input[i]
        
        if max_value < input[i]:
            max_value = input[i]

        total += input[i]

    return {'minimum': min_value, 'maximum': max_value, 'length': len(input), 'average': float(total) / len(input)}


class StatsCalculatorShould(unittest.TestCase):
    def _get_sorted_keys_from_stats(self, stats):
        keys = list(stats.iterkeys())
        keys.sort()
        return keys

    def test_given_list_with_min_value_of_2_return_correct_min_stats(self):
        input = [2,3,4]

        stats = stats_calculator(input)

        self.assertEquals(stats['minimum'], 2)

    def test_given_list_with_min_value_of_3_return_correct_min_stats(self):
        input = [3,4,5]

        stats = stats_calculator(input)

        self.assertEquals(stats['minimum'], 3)

    def test_given_list_with_min_value_of_4_return_correct_min_stats(self):
        input = [6,4,5]

        stats = stats_calculator(input)

        self.assertEquals(stats['minimum'], 4)

    def test_given_list_with_max_value_9_return_correct_max_stat(self):
        input = [9, 1, 4]

        stats = stats_calculator(input)

        self.assertEquals(stats['maximum'], 9)

    def test_given_list_with_max_value_1_return_correct_max_stat(self):
        input = [-9, 1, -4]

        stats = stats_calculator(input)

        self.assertEquals(stats['maximum'], 1)

    def test_given_list_with_max_8_return_correct_stat(self):
        input = [1,2,3,4,5,6,7,8]

        stats = stats_calculator(input)

        self.assertEquals(stats['maximum'], 8)

    def test_stats_is_constructed_with_the_required_elements(self):
        input = [1]

        stats = stats_calculator(input)

        self.assertTrue(isinstance(stats, dict))
        self.assertEquals(self._get_sorted_keys_from_stats(stats), ['average', 'length', 'maximum', 'minimum'])

    def test_given_list_of_2_stats_returns_correct_list_length(self):
        input = [1, 2]

        stats = stats_calculator(input)

        self.assertEquals(stats['length'], 2)

    def test_given_list_with_sigle_value_it_returns_the_right_average(self):
        input = [1]

        stats = stats_calculator(input)

        self.assertEquals(stats['average'], 1)

    def test_given_list_with_two_values_it_returns_the_right_average(self):
        input = [1, 2]

        stats = stats_calculator(input)

        self.assertEquals(stats['average'], 1.5)


if __name__ == '__main__':
    unittest.main()