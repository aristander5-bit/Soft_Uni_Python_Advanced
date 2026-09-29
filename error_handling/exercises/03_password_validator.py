class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

SPECIALS = {"@", "*", "&", "%"}

def pwd_too_common(pwd, specials):
    only_digits = pwd.isdigit()
    only_char = pwd.isalpha()
    only_specials = all(ch in specials for ch in pwd)
    return only_digits or only_char or only_specials

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 character")

    if pwd_too_common(password, SPECIALS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIALS for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")