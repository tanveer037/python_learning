def is_palindrome(given_string):
    if given_string == given_string[::-1]:
        return True
    return False