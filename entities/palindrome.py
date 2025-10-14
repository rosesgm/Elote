class Palindrome:
    def __init__(self, phrase):
        self.phrase = phrase

    def is_palindrome(self) -> bool:
        p = self.phrase
        # Si es palindromo retorna true y si no retorna false
        p = p.lower().replace(" ", "")

        palindrome = p[::-1]
        if p == palindrome:
            return True
        else:
            return False
