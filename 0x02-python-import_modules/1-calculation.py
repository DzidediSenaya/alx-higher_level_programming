#!/usr/bin/python3
a = 10
b = 5

import calculator_1

add_result = calculator_1.add(a, b)
sub_result = calculator_1.sub(a, b)
mul_result = calculator_1.mul(a, b)
div_result = calculator_1.div(a, b)

print("{} + {} = {}".format(a, b, add_result))
print("{} - {} = {}".format(a, b, sub_result))
print("{} * {} = {}".format(a, b, mul_result))
print("{} / {} = {}".format(a, b, div_result))

