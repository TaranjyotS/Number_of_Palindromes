# Number_of_Palindromes
The project aims on finding all possible palindromes in a given string. Unit test cases are included in the project so as to ensure that all code is up to the quality standards.

Note - One character strings are not considered palindromes in the given project.


The project proceeds by laying out 3 necessary functions:
1. find_palindrome - Checks if the substring of a given string is palindrome or not.
2. solution - Initializes loop which checks for the same character at position 1(start) in the string ahead, marks it as a substring, and checks if it is a palindrome or not. Then the start position is incremented by 1. After covering all the palindromic substrings, a list of palindromic substrings is created and sorted in reverse order by length. In the end, all palindromic substrings are printed along with their length and position of the starting character of the substring in the given string.
3. test_is_palindrome - Checks if both the functions are working properly by running some unit tests on them. The solution() function is run through a series of different arbitrary strings(characters, numbers, special characters) to check for palindromic substrings. The test case that fails the unit test is presented by "F" in the output terminal.
