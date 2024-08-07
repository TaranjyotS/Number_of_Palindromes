# Number_of_Palindromes
The project aims on finding all possible palindromes in a given string. Unit test cases are included in the project so as to ensure that all code is up to the quality standards. The program is coded in Python language.


**Note** - One character strings are not considered palindromes in the given project.

## How it works
The project proceeds by laying out 2 necessary functions:

1. *find_palindrome* - Checks if the substring of a given string is palindrome or not.
2. *number_of_palindromes* - Initializes loop which checks for the same character at position 1(start) in the string ahead, marks it as a substring, and checks if it is a palindrome or not. Then the start position is incremented by 1. After covering all the palindromic substrings, a list of palindromic substrings is created and sorted in reverse order by length. In the end, all palindromic substrings are printed along with their length and position of the starting character of the substring in the given string.

## Complexity
The complexities for the given program are
1. Space compexity - O(n)
2. Time complexity - O(n^2)

**Note** - To run an arbitrary string, just call the function number_of_palindromes() with input as the string you want to run for checking the number of palindromes in.
