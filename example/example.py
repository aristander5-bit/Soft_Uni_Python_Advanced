# file = open("example.txt")
# print(file.read())
# print(file.mode)
# print(file.closed)
# print(file.name)

import os

path = os.path.abspath(__file__)
path_to_dir = os.path.dirname(__file__)
print(os.path.abspath(__file__))
print(path_to_dir)