def is_palindrome(str):
        n_str = str.lower()
        revers_str = ""
        for char in n_str:
                revers_str = char + revers_str
        if n_str == revers_str:
                return True
        else:
                return False
