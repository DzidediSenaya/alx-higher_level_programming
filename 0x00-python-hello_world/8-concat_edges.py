#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[str.find("object"):str.find("object") + 25], end="")
print(str[str.find("Python"):])
