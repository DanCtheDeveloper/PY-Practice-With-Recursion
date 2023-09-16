# Write code for algorithm 5 below
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str = ''.join(s.lower().split())
    return cleaned_str == cleaned_str[::-1]

# Example usage
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
