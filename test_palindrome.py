# Unit Testing the functions to mark safe deployment of the code.

import unittest

from palindrome import find_palindrome, number_of_palindromes

class TestPalindromes(unittest.TestCase):
    """Test a given string for palindromes.
    """

    def test_is_palindrome(self):
        # Testing find_palindrome() function to see it gives right resuts.
        assert find_palindrome('ARA') is True 
        assert find_palindrome('ILOVEUEVOLI') is True

    def test_number_of_palindromes(self):
        # Testing number_of_palindromes() function to get if there is any palindrome present in the given string.
        assert number_of_palindromes('ABCBAHELLOHOWRACECARAREYOUILOVEUEVOLIIAMAIDOINGGOOD') != 0
        assert number_of_palindromes("1234543223454531123211") != 0
        assert number_of_palindromes("!aabbccaaccbbaa!")  != 0
        assert number_of_palindromes("@!#&@$%&@!@&!")  != 0
        assert number_of_palindromes("a23432a43234a") != 0
        assert number_of_palindromes('adgbuyebjkao') == 0

if __name__ == '__main__':
    unittest.main()
