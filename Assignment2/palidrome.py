#  Module for checking palindromes with preprocessing to remove non-lowercase characters.
#  Functions:
#   remove_non_lowercase(k): Removes all characters from the input string that are not lowercase English letters ('a'-'z').
#   palindrome(s): Checks if the input string is a palindrome, ignoring case and non-lowercase characters.


def remove_non_lowercase(k):
   
    for i in range(32, 97):
        k = k.replace(chr(i), '')
    # Remove ASCII characters `{`, `|`, `}`, and `~` (123 to 126)
    for i in range (123, 127):
        k = k.replace(chr(i), '')
    return k



def palindrome(s):
    s = s.lower()
    l = len(s)
    reverse = remove_non_lowercase(s[::-1])
    if (l < 2):
        return True
    elif s[0] == s[l -1]:
        return True
    else:
        return False
    
    