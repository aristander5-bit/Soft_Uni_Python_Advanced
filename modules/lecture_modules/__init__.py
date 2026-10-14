class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


SPECIAL_SYMBOLS = ["@", "*", "&", "%"]
password = input()

while password != "Done":
    if len(password) < 8:
        raise PasswordTooShortError('Password must contain at least 8 characters')

    if password.isdigit() or password.isalpha() or all(char in SPECIAL_SYMBOLS for char in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if " " in password:
        raise PasswordContainsSpacesError('Password must not contain empty spaces')

    has_special = any(char in SPECIAL_SYMBOLS for char in password)
    if not has_special:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    print("Password is valid")
    password = input()