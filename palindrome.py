import re

def find_palindrome(string):
    """Finds and returns a boolean if a given string is palindrome.

    Args:
        string: The string for which we want to check if palindrome or not.

    Returns:
        True, if a given string is palindrome.
    """
    return string == string[::-1]

def number_of_palindromes(string):
    """Returns the number of palindromes in a given string.

    Args:
        string: The string for which we want to check if palindrome or not.

    Returns:
        total_palindromes: Numner of palindrome in a given string.
    """
    palindrome_list = []
    total_palindromes = 0
    for i in range(len(string)):
        start = string[i]
        same_char = string[i::]
        # re.finditer yields match objects matching the regex pattern in a string.
        for match in re.finditer(start, same_char):
            if match.start()!=0:
                sub_string = same_char[0:match.start()+1:]
                
                if find_palindrome(sub_string) == True:
                    total_palindromes += 1
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
        print("Number of palindromes in the string are", total_palindromes)
        # Printing palindromes with their length and position.
        for i in palindrome_list:
            print(i[:len(i)-2:],",", len(i[:len(i)-2:]),",",i[len(i)-2:len(i):])
        print("\n")

    return total_palindromes
