#!/usr/bin/env python3

# Break long import line into two
a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__(
    '4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

# Break lines to respect the 79-character limit
print("a is a {} with a value of {}".format(
    type(a), a))
print("pi is a {} with a value of {}".format(
    type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(
    type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(
    type(school), school))
