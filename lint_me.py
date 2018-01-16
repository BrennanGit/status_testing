#!/usr/bin/env python2
"""This file should pass on flake8 linting"""


class NewClass(object):

    def __init__(self, value):
        self.set_member(value)

    def set_member(self, value):
        self.member = value

    def get_member(self):
        return self.member


my_object = NewClass('this')
print(my_object.get_member())  # should print 'this'
my_object.set_member('that')
print(my_object.get_member())  # should print 'that'
