def is_palindrome(phrase):
    # Indices at front and back
    left = 0
    right = len(phrase) - 1

    while (left < right):
        # Iterate each until alphanumeric character is found
        while ((not phrase[left].isalnum()) and (left < right)):
            left += 1
        while ((not phrase[right].isalnum()) and (right > left)):
            right -= 1

        # Compare in same case, continue if same, return false otherwise
        if phrase[left].lower() != phrase[right].lower():
            return False

        left += 1
        right -= 1

    return True


assert is_palindrome("")
assert is_palindrome("a")
assert is_palindrome("doggod")
assert is_palindrome("dogod")
assert is_palindrome("A man, a plan, a canal, Panama.")
assert is_palindrome("Able was I, ere I saw Elba!")
assert not is_palindrome("Ray a Ray")
assert is_palindrome("!@#$^&*(__(^$#^")
assert is_palindrome("Madam, I'm Adam.")
assert is_palindrome("Madam, 'm Adam.")
assert not is_palindrome("Mdam, 'm Adam.")
assert not is_palindrome("Word")
