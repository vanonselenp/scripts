import unittest


def anagram(original):
    if len(original) == 1:
        return [original]

    create_anagrams = set()

    for i in range(len(original)):
        character = original[i]
        sub_string = original[:i:] + original[i + 1::]
        potentials = anagram(sub_string)
        for word in potentials:
            create_anagrams.add(character + word)
            create_anagrams.add(word + character)

    anagrams = list(create_anagrams)
    anagrams.sort()
    return anagrams


class AnagramShould(unittest.TestCase):
    def test_return_character_a_given_single_character(self):
        actual = anagram("a")

        self.assertEquals(actual, ["a"])

    def test_return_character_b_given_single_character(self):
        anagrams = anagram("b")

        self.assertEquals(anagrams, ["b"])

    def test_return_two_possible_anagrams_given_two_characters_ab(self):
        anagrams = anagram('ab')

        self.assertEquals(anagrams, ['ab', 'ba'])

    def test_return_two_possible_anagrams_given_two_characters_cd(self):
        anagrams = anagram('cd')

        self.assertEquals(anagrams, ['cd', 'dc'])

    def test_return_two_possible_anagrams_given_two_characters_ed(self):
        anagrams = anagram('de')

        self.assertEquals(anagrams, ['de', 'ed'])

    def test_return_single_anagram_given_two_characters_aa(self):
        anagrams = anagram('aa')

        self.assertEquals(anagrams, ['aa'])

    def test_return_three_possible_anagrams_given_three_characters_aab(self):
        anagrams = anagram('aab')

        self.assertEquals(anagrams, ['aab', 'aba', 'baa'])

    def test_return_six_possible_anagrams_given_characters_abc(self):
        actual = anagram("abc")

        self.assertEquals(actual, ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_return_24_possible_anagrams_given_four_characters_brio(self):
        anagrams = anagram("brio")

        self.assertEquals(len(anagrams), 24)


if __name__ == '__main__':
    unittest.main()