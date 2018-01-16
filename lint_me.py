#!/usr/bin/env python2
"""This file should fail on flake8 linting

lint_me.py:4:1: E302 expected 2 blank lines
lint_me.py:15:1: E305 expected 2 blank lines after class or function definition
lint_me.py:16:30: E261 at least two spaces before inline comment
lint_me.py:18:30: E261 at least two spaces before inline comment
"""

class NewClass(object):

    def __init__(self, value):
        self.set_member(value)

    def set_member(self, value):
        self.member = value

    def get_member(self):
        return self.member

my_object = NewClass('this')
print(my_object.get_member()) # should print 'this'
my_object.set_member('that')
print(my_object.get_member()) # should print 'that'
