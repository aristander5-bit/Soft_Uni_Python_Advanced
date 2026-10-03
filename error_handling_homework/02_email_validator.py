class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

DOMAINS = (".com", ".bg", ".org", ".net")

email = input()

while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@", 1)

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not domain.endswith(DOMAINS):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()