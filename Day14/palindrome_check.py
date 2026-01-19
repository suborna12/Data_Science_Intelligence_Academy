def is_palindrome(input_string):
    return input_string == input_string[::-1]

s1 = "radar"
s2 = "hello"
r1 = is_palindrome(s1)
r2 = is_palindrome(s2)
print(r1)
print(r2)
