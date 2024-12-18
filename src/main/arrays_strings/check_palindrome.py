
class PalindromeChecker:
    def __init__(self, text):
        self.text = text

    def is_palindrome(self):
        left = 0
        right = len(self.text)-1
        while left < right:
            if self.text[left] != self.text[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


if __name__ == '__main__':
    text = "ababa"
    checker = PalindromeChecker(text)
    if checker.is_palindrome():
        print("Palindrome")
    else:
        print("Not Palindrome")



