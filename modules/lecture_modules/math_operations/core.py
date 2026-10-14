mapper = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x ** y,
}

def calculate(num_1, num_2, sign):
    function = mapper[sign]
    return function(num_1, num_2)
