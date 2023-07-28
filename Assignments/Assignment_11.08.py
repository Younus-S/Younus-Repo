def is_palindrome(pal):
    if pal == pal[::-1]:
        print(pal,"is a palindrome")
    else:
        print(pal,"is not a palindrome")

is_palindrome("radar")
is_palindrome("python")