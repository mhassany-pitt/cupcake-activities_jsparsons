def is_palindrome(str):
        i = 0
        j = len(str) - 1
        n_str = str.lower()
        while i < j:
                if n_str[i] != n_str[j]:
                        return False
                i += 1
                j -= 1
        return True
