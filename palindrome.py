import re

# Function to check if the string is palindrome or not.
def find_palindrome(s):
    return s == s[::-1]

def solution(s):
    palindrome_list = []
    no_of_palindromes = 0
    for i in range(len(s)):
        start = s[i]
        same_char = s[i::]
        # re.finditer yields match objects matching the regex pattern in a string.
        for match in re.finditer(start, same_char):
            if match.start()!=0:
                sub_string = same_char[0:match.start()+1:]
                
                if find_palindrome(sub_string) == True:
                    no_of_palindromes += 1
                    if i<10:
                        sub_string = sub_string+str(0)+str(i)
                    else:
                        sub_string = sub_string+str(i)
                    
                    # Append all the substring palindromes into a new list.
                    palindrome_list.append(sub_string)
                    # Sorting the new palindrome list by the length of the substring in reverse order.
                    palindrome_list = sorted(palindrome_list, key=lambda palindrome_list: (-len(palindrome_list),palindrome_list))
    
    if len(palindrome_list) == 0:
        print("No palindromes in the given string.")            
    else:
        print("Number of palindromes in the string are", no_of_palindromes)
        # Printing palindromes with their length and position.
        for i in palindrome_list:
            print(i[:len(i)-2:],",", len(i[:len(i)-2:]),",",i[len(i)-2:len(i):])
        print("\n")

    return no_of_palindromes

solution("ABCBAHELLOHOWRACECARAREYOUILOVEUEVOLIIAMAIDOINGGOOD")
#solution("1234543223454531123211")
#solution("!aabbccaaccbbaa!")
#solution("@!#&@$%&@!@&!")
#solution("a23432a43234a")
#solution("adgbuyebjkao")

# Unit Testing the functions to mark safe deployment of the code.
import unittest

class TestPalindromes(unittest.TestCase):

    def test_is_palindrome(self):
        # Testing find_palindrome() function to see it gives right resuts.
        assert find_palindrome('ARA') is True 
        assert find_palindrome('ILOVEUEVOLI') is True

        # Testing solution() function to get if there is any palindrome present in the given string.
        assert solution('ABCBAHELLOHOWRACECARAREYOUILOVEUEVOLIIAMAIDOINGGOOD') != 0
        assert solution("1234543223454531123211") != 0
        assert solution("!aabbccaaccbbaa!")  != 0
        assert solution("@!#&@$%&@!@&!")  != 0
        assert solution("a23432a43234a") != 0
        assert solution('adgbuyebjkao') != 0  
        
if __name__ == '__main__':
    unittest.main()
